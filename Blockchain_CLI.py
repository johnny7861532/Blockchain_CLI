#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:33:18 2018

@author: johnnyhsieh
"""


import click
import subprocess




__author__ = "Johnny Hsieh"



@click.group()
def Blockchain():
    """                                                                        
    Very simple CLI to start a different protocol from local.
    Supporting NEO and ICON.
    """
    pass




@Blockchain.command(help="Choose the network you want to conncet.")
@click.option('--networkid', type=click.Choice(['testnet', 'mainnet']),prompt=True)  
def StartNEO(networkid):
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
    
 

@Blockchain.command(help="Install the NEO kit inorder to start NEO node.")
def installNEO():

    click.confirm('This commend will install neo-python, Do you want to continue?', abort=True)
    subprocess.call(["pip3","install","neo-python"]) 
    subprocess.call(["git","clone","https://github.com/CityOfZion/neo-python.git"])
    click.echo(click.style('NEO', fg='green', blink=True, bold=True))
    click.echo(click.style('Envirment is ready! You can start a NEO node by typing ',bg='black', fg='white'))
    click.echo(click.style('python3 Blockchain_CLI.py startneo',bg='white', fg='red'))
    
@Blockchain.command(help="Install the ICON kit inorder to start ICON node.")
def installICON():
   
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
    
@Blockchain.command(help="Start ICON node and begin to interact with tbears.")
def startICON():
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is init!',bg='black', fg='white'))
    subprocess.call(["brew", "services", "start" ,"rabbitmq"]) 
    subprocess.call(["tbears", "start"]) 
    subprocess.call(["tbears","command","-h"])
    subprocess.call(["tbears", "start"]) 
    subprocess.call(["tbears", "lastblock"]) 
    
    
@Blockchain.command(help="Stop ICON node and close rabbitmq and tbears.")
def stopICON():
    subprocess.call(["brew", "services", "stop" ,"rabbitmq"]) 
    subprocess.call(["tbears","stop"])
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('Node is kill',bg='black', fg='white'))
    
@Blockchain.command(help="Using ICON template ABCToken to test simple contract.")
def ICONContracttest():
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('contract depolying....',bg='black', fg='white'))  
    subprocess.call(["tbears","init", "abc", "ABCToken"])
    subprocess.call(["tbears","ls","abc"])
    subprocess.call(["tbears", "deploy", "-t","tbears","abc"])
    click.echo(click.style('Please using this command to get the result:',bg='black', fg='white'))
    click.echo(click.style('python3 Blockchain_CLI.py geticontx tx',bg='black', fg='red'))
    click.echo(click.style('Please using this command to get the result:',bg='black', fg='white'))
    click.echo(click.style('python3 Blockchain_CLI.py geticoncontractapi tx',bg='black', fg='red'))
    
@Blockchain.command(help="Get the result from txhash")
@click.argument('tx')
def getICONtx(tx):
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('get tx result:',bg='black', fg='white'))  
    subprocess.call(["tbears","txresult", tx])
    
    
@Blockchain.command(help="Get the contract api")
@click.argument('tx')  
def getICONapi(tx):
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('get contract api:',bg='black', fg='white'))  
    subprocess.call(["tbears","scoreapi",tx])
    
@Blockchain.command(help="Run the unittest of contract")
@click.argument('project')  
def ICONUnittest(project):
    click.echo(click.style('ICON', fg='green', blink=True, bold=True))
    click.echo(click.style('testing ICON contract',bg='black', fg='white'))  
    subprocess.call(["tbears","test",project])
    
    
    

if __name__ == '__main__':
    """                                                                        
    Very simple CLI to start a different protocol from local.
    """
    Blockchain()
