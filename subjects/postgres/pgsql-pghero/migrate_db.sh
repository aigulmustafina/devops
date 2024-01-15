#!/bin/bash
set -e

psql -U postgres deadline < /backup/dump.sql
