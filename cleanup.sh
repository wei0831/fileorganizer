yapf ./src/ --recursive -i


if [ -d "./src/log" ]; then
    rm ./src/log -r
fi