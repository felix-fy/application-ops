#!/bin/bash
JAVA_HOME=/usr/local/java/jdk/jdk1.8.0_131
JRE_HOME=/usr/local/java/jdk/jdk1.8.0_131/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH
