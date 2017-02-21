#!/bin/sh
sudo rm *.java *.class *.tokens
antlr4 ClusterConfig.g4
javac *.java

