yapf ./fileorganizer/ --recursive -i


if [ -d "./log" ]; then
    rm ./log -r
fi
if [ -d "./fileorganizer/log" ]; then
    rm ./fileorganizer/log -r
fi