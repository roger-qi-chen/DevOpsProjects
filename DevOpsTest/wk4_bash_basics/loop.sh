#!/usr/bin/env sh

DURATION=4
COUNT=1
ATTEMPTS=40
PROFILER_SH="/Applications/Docker.app/Contents/MacOS/com.docker.supervisor"
while [ $COUNT -lt $ATTEMPTS ] && [ -n "$(pgrep -f "${PROFILER_SH}")" ]; do
    echo "Waiting ${DURATION} seconds for process ${PROFILER_SH} to complete. This is attempt number $((COUNT))"
    sleep "$DURATION"
    COUNT=$((COUNT+1))
done

echo "Exited the loop"