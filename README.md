
# ProFTPD-1.3.3c-Backdoor_Command_Execution

# Description
On Sunday, the 28th of November 2010 around 20:00 UTC the main distribution server of the ProFTPD project was compromised. The attackers most likely used an unpatched security issue in the FTP daemon to gain access to the server and used their privileges to replace the source files for ProFTPD 1.3.3c with a version which contained a backdoor. The unauthorized modification of the source code was noticed by Daniel Austin and relayed to the ProFTPD project by Jeroen Geilman on Wednesday, December 1 and fixed shortly afterwards. 

Anyone who downloaded ProFTPD 1.3.3c from one of the official mirrors from 2010-11-28 to 2010-12-02 will most likely be affected by the problem. The backdoor introduced by the attackers allows unauthenticated users remote root access to systems which run the maliciously modified version of the ProFTPD daemon. 

# Installation
Make sure you have netcat installed on your attacker system. To install the requirments for the script to run sucessfully use:

<pre>pip3 install -r requirements.txt</pre>


# Exploitation

<img src="https://media.giphy.com/media/H0MrdSE07wtLGZOF8Q/giphy.gif">

# Download Proftpd 1.3.3c (Backdoored Version)

Download the backdoored version from the bellow given link:<br>
<a href="http://www.exploit-db.com/application/15662/" target="_blank">http://www.exploit-db.com/application/15662/</a>


# Learn More (Resources)

<a href="https://www.aldeid.com/wiki/Exploits/proftpd-1.3.3c-backdoor" target="_blank">https://www.aldeid.com/wiki/Exploits/proftpd-1.3.3c-backdoor</a>
<a href="https://www.rapid7.com/db/modules/exploit/unix/ftp/proftpd_133c_backdoor" target="_blank">https://www.rapid7.com/db/modules/exploit/unix/ftp/proftpd_133c_backdoor</a>








