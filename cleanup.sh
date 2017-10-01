yapf setup.py -i
yapf ./fileorganizer/ --recursive -i

if [ -d "./build" ]; then
    rm -rf ./build
fi
if [ -d "./dist" ]; then
    rm -rf ./dist
fi
if [ -d "./temp" ]; then
    rm -rf ./temp
fi
if [ -d "./fileorganizer.egg-info" ]; then
    rm -rf ./fileorganizer.egg-info
fi
if [ -d "./log" ]; then
    rm -rf ./log
fi
if [ -d "./fileorganizer/log" ]; then
    rm -rf ./fileorganizer/log
fi
if [ -d "./fo_log" ]; then
    rm -rf ./fo_log
fi