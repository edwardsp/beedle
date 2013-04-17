#!/bin/sh

BOARD=<ENTER-BOARD-ID>
KEY=<ENTER-KEY>
TOKEN=<ENTER-TOKEN>

wget -O data.json --no-check-certificate "https://api.trello.com/1/boards/${BOARD}?key=${KEY}&token=${TOKEN}&actions=all&actions_limit=1000&cards=all&lists=all&members=all&member_fields=all&checklists=all&fields=all"


