# THis probably doesn't work all the time still need to flush out this 
sudo apt-get install python3-venv
mdkir venv
cd venv
pyhon3 -m venv env
cd ../
source venv/env/bin/activate

##TODO MAKE THIS DOCKER##

##INSTALL REQUIRMENTS#
./installRequirments.bash

#TODO Compile for the first time
pip install buildozer
#this creates the .spec file which whree we specify the python libs we need to include in the project
#Also where the andriod permissions are specified
buildozer init

buildozer -v android debug

#If you run into build issues don't foreget to blow away your buildozer folder
rm -rfv .buildozer

#or This fixes the cython can't build issue
buildozer andriod debug

#TODO build CYTHON from scratch.
git clone https://github.com/cython/cython.git
cd cython
python setup.py install
python3 setup.py install

#TODO Fix python lib enum for buildozer.spec currently doesn't want to install

#Not sure if this will work since it has c files that need to bget compiled into our build
sudo apt-get install python3-pyaudio
sudo apt-get install portaudio19-dev
brew install portaudio
sudo apt-get install -y lld
#May need to manually compile and install port audio
git clone https://github.com/PortAudio/portaudio.git
cd portaudio
./configure
make -j 4
sudo make install
