#!/bin/sh

set -e

cmd="$@"

until PGPASSWORD=$DATABASE_PASSWORD psql -h $DATABASE_HOST -U $DATABASE_USER -q -c '\q' 2>/dev/null; do
  >&2 echo "Retrying to connect to postgres"
  sleep 1
done

exec $cmd
