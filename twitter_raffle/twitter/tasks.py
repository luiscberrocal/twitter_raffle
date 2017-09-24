from celery import shared_task, Task

from twitter_raffle.twitter.models import AsyncActionReport
from .utils import SearchTwitterUtil
import logging

logger = logging.getLogger(__name__)

class BaseErrorHandlerMixin:
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        '''
        exc – The exception raised by the task.
        task_id – Unique id of the failed task.
        args – Original arguments for the task that failed.
        kwargs – Original keyword arguments for the task that failed.
        '''
        AsyncActionReport.objects.filter(id=kwargs['async_action_report_id']) \
            .update(status=AsyncActionReport.FAILED,
                    message=str(exc),
                    error_traceback=einfo)

    def on_success(self, retval, task_id, args, kwargs):
        '''
        retval – The return value of the task.
        task_id – Unique id of the executed task.
        args – Original arguments for the executed task.
        kwargs – Original keyword arguments for the executed task.
        '''
        logger.debug('Added {} tweets'.format(retval))
        AsyncActionReport.objects.filter(id=kwargs['async_action_report_id']) \
            .update(status=AsyncActionReport.OK,
                    message='Added {} tweets'.format(retval),
                    message_type= AsyncActionReport.INFO)

class ThirdPartyBaseTask(BaseErrorHandlerMixin, Task):
    pass

@shared_task(base=ThirdPartyBaseTask)
def fetch_and_store_tweets(search_query, **kwargs):
    search_util = SearchTwitterUtil()
    return search_util.search(search_query)


@shared_task
def fetch_data_and_store_it(search_query):
    async_action_report = AsyncActionReport.objects.create(message='Started querying for {}'.format(search_query))
    t1 = fetch_and_store_tweets.s(search_query, async_action_report_id=async_action_report.id)

    return t1.delay()
