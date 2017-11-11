# pliers-docker
Docker setup for pliers

[Pliers](https://github.com/tyarkoni/pliers) is a tool for video annotation by Tal Yarkoni's team.  
It has a pretty hairy stack of dependencies so it made sense to containerize it.

Another tricky aspect of running pliers is that it requires credentials for several different web APIs,
which we certainly don't want to include in the container!  We deal with this by requiring the user
to create a bash script to set the appropriate environment variables for those API credentials,
and then source it upon executing the container.  There are almost certainly more elegant ways to do this
but it works well enough.

To use it:

1. Build the docker container:

    docker build -t pliers .

2. Create a file that contains all of the relevant API keys, called env.sh:

```
export WIT_AI_API_KEY="abc123"
export IBM_USERNAME="joe@schmo.edu"
export IBM_PASSWORD="xyzabc"
export INDICO_APP_KEY="abcyyz"
export GOOGLE_APPLICATION_CREDENTIALS="/root/share/googleapi.json"
export CLARIFAI_API_KEY="hhhvvv"
```
This should be obvious, but just in case: NEVER check this file into a github repository, unless you want to buy free cloud computing for a cybercriminal.

3. Obtain a service account key for your Google Cloud account, and save it to a file called googleapi.json

4. Open an interactive session on the docker container:

    docker run -it -v /path/to/pliers-docker:/root/share pliers /bin/bash
    
where /path/to/pliers-docker contains the files generated above.

5. Set up the python environment:

    . setup.sh

At this point you should have a python environment that is ready for you to start using pliers.
