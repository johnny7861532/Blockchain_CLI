#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:33:18 2018

@author: johnnyhsieh
"""


import click
import subprocess
from time import sleep




__author__ = "Johnny Hsieh"



@click.group()
def Blockchain():
    """                                                                        
    Very simple CLI to start a different protocol from local.
    Supporting NEO
    """
    pass




@Blockchain.command()
@click.option('--networkid', type=click.Choice(['testnet', 'mainnet']),prompt=True)  
def StartNEO(networkid):
    """
    Choose the network you want to conncet.
    """
    if networkid == "testnet":
        initTestnet()
    else:
        initMainnet()


def initTestnet():
    click.echo(click.style('NEO', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is init!',bg='black', fg='white'))
    subprocess.call(["cd","neo-python"]) 
    subprocess.call(["np-prompt"])

    

def initMainnet():
    click.echo(click.style('NEO', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is init!',bg='black', fg='white'))
    subprocess.call(["cd","neo-python"]) 
    subprocess.call(["np-prompt","-m"])
    
 

@Blockchain.command()
def installNEO():
    """
    Install the NEO kit inorder to start NEO node.
    """
    click.confirm('This commend will install neo-python, Do you want to continue?', abort=True)
    subprocess.call(["pip3","install","neo-python"]) 
    subprocess.call(["git","clone","https://github.com/CityOfZion/neo-python.git"])
    click.echo(click.style('NEO', fg='green', blink=True, bold=True))
    click.echo(click.style('Envirment is ready! You can start a NEO node by typing ',bg='black', fg='white'))
    click.echo(click.style('python3 Blockchain_CLI.py startneo',bg='white', fg='red'))
    
@Blockchain.command()
def installICON():
    """
    Install the ICON kit inorder to start ICON node.
    """
    click.confirm('This commend will install mutilple libraries, Do you want to continue?', abort=True)
    subprocess.call(["brew","install","leveldb"])
    subprocess.call(["brew","install","rabbitmq"]) 
    subprocess.call(["brew","install","automake"]) 
    subprocess.call(["brew","install","pkg-config"]) 
    subprocess.call(["brew","install","libtool"]) 
    subprocess.call(["brew","install","libffi"]) 
    subprocess.call(["brew","install","gmp"]) 
    subprocess.call(["pip3", "install", "tbears"])
    click.echo(click.style('Icon', fg='green', blink=True, bold=True))
    click.echo(click.style('Envirment is ready! You can start a ICON node by typing ',bg='black', fg='white'))
    click.echo(click.style('python3 Blockchain_CLI.py starticon',bg='white', fg='red'))
    
@Blockchain.command()
def startICON():
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is init!',bg='black', fg='white'))
    subprocess.call(["brew", "services", "start" ,"rabbitmq"]) 
    subprocess.call(["tbears", "start"]) 
    subprocess.call(["tbears","command","-h"])
    subprocess.call(["tbears", "start"]) 
    subprocess.call(["tbears", "lastblock"]) 
    
    
@Blockchain.command()
def stopICON():
    subprocess.call(["brew", "services", "stop" ,"rabbitmq"]) 
    subprocess.call(["tbears","stop"])
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is kill',bg='black', fg='white'))
    

if __name__ == '__main__':
    """                                                                        
    Very simple CLI to start a different protocol from local.
    """
    Blockchain()