#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

celery -A twitter_raffle.taskapp worker -l INFO
