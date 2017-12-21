#!/bin/sh

search_string="youtube + $@"
geturl="$(googler -C --np --count=2 $search_string | grep http | head -n 1)"
mpsyt playurl $geturl 
