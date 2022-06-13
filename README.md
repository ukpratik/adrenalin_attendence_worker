Hello, this is Light Yagami, username 'MX_WrdXX', creator of this script.

For the Employee Peace,
This script has been created to get rid of daily signin and signout shit for attendence at Adrenalin.

This script can be used by any employee who is the member of group "XX-Employees_Underground-XX" (Short - XEUX)


Adrenalin Attendence Auto Sign In and Signout

Rules of XEUX:
> Due to conern of confidentiality, the information about this group should be shared to trusted HOMO SAPIENS only.
> As of Living in the world of Humans, Trust and honesty of all members is expected on this platform.
> This platform is created for the peace, happiness, rights and solutions of employees all over the planet. (and for Fun, of course ':) )


.
.
.

Cron settings and commands to install the script:

first go to crontab file:

$ sudo nano /etc/crontab

Add these elow lines(example. change accrodingly):

############### Adrenalin Signin and signout shit ###############

45 9    * * *   root    python3 /home/pratik/Desktop/adrenalin_attendence_worker-main/attendence_shit.py

45 19   * * *   root    python3 /home/pratik/Desktop/adrenalin_attendence_worker-main/attendence_shit.py

##################################################################

<comment headline>
  
  time_scheduling user <script>    // for sign-in
  
  time_scheduling user <script>    // for sign-out

<comment-end>
  
Here <script> is : python3 path of script    // remember attendence_shit.py is the main file that needs to be called/executed for automation
  
After this:
  
  Restart the cron service using the following commands:
  
  $ sudo service cron reload
    
  $ systemctl restart cron
  
Done!
  
Have a nice day!
