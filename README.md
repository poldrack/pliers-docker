# pliers-docker
Docker setup for pliers

[Pliers](https://github.com/tyarkoni/pliers) is a tool for video annotation by Tal Yarkoni's team.  
It has a pretty hairy stack of dependencies so it made sense to containerize it.

Another tricky aspect of running pliers is that it requires credentials for several different web APIs,
which we certainly don't want to include in the container!  We deal with this by requiring the user
to create a bash script to set the appropriate environment variables for those API credentials,
and then source it upon executing the container.  There are almost certainly more elegant ways to do this
but it works well enough.
