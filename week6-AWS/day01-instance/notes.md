## Week 6 – Day 1 Notes — AWS EC2 & Ubuntu

## AWS EC2 Basics

Today we learned about AWS EC2 Instances and how to connect Ubuntu servers using the terminal.

## What is EC2?

EC2 (Elastic Compute Cloud) is a virtual server provided by Amazon Web Services.

It allows us to:

- Launch virtual machines
- Choose operating systems
- - Configure storage and networking
- Run applications in the cloud
- Launching an EC2 Instance

## Main steps:

- Login to AWS Console
- Open EC2 Dashboard
- Launch Instance
- Select Ubuntu AMI
- Choose instance type
- Create key pair
- Configure security group
- - Launch instance
    Connecting Ubuntu using Terminal

We connected the Ubuntu EC2 instance using SSH from the local terminal.

## Example command:

ssh -i key.pem ubuntu@your-public-ip
Commands Practiced

## Check files:

ls

## Update packages:

sudo apt update

Install packages:

sudo apt install python3

## Check system info:

uname -a

## What I Learned Today

- Basics of AWS EC2
- Launching Ubuntu instances
- Connecting EC2 using SSH
- Running Linux commands from terminal
- Managing cloud servers remotely
