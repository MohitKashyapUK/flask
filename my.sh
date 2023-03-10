su -
apt-get update -y
apt-get upgrade -y
apt-get install -y make git zlib1g-dev libssl-dev gperf cmake clang libc++-dev libc++abi-dev
exit
git clone --recursive https://github.com/tdlib/telegram-bot-api.git
cd telegram-bot-api
rm -rf build
mkdir build
cd build
CXXFLAGS="-stdlib=libc++" CC=/usr/bin/clang CXX=/usr/bin/clang++ cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=.. ..
cmake --build . --target install
cd ../..
ls -l telegram-bot-api/bin/telegram-bot-api*

cd telegram-bot-api/
cd bin/
./telegram-bot-api --api-id=$TELEGRAM_API_ID --api-hash=$TELEGRAM_API_HASH
