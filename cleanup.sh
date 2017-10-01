yapf setup.py -i
yapf ./fileorganizer/ --recursive -i

if [ -d "./build" ]; then
    rm ./build -r
fi
if [ -d "./dist" ]; then
    rm ./dist -r
fi
if [ -d "./temp" ]; then
    rm ./temp -r
fi
if [ -d "./fileorganizer.egg-info" ]; then
    rm ./fileorganizer.egg-info -r
fi
if [ -d "./log" ]; then
    rm ./log -r
fi
if [ -d "./fileorganizer/log" ]; then
    rm ./fileorganizer/log -r
fi
if [ -d "./fo_log" ]; then
    rm ./fo_log -r
fi