yapf ./src/ --recursive -i


if [ -d "./log" ]; then
    rm ./log -r
fi
if [ -d "./src/log" ]; then
    rm ./src/log -r
fi