RUN echo "I'm grooty, you should be too"
RUN mkdir -p /home/@(name)
RUN echo "export PS1='\[\033[01;32m\]\u \@@ foobar\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /home/@(name)/.bash_profile
