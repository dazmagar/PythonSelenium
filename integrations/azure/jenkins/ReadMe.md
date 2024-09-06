### Building a browser-based test automation server with Jenkins on Azure by using PythonSelenium

(**2022 NOTE:** Steps from [this 2019 tutorial from Boston Code Camp](https://www.bostoncodecamp.com/CC31/sessions/details/16741) are now **out-of-date**. For installing Jenkins from the Azure Marketplace, you can try using [Bitnami Jenkins](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/bitnami.jenkins). **Or**, for the newer official Microsoft tutorial, see [Get Started: Install Jenkins on an Azure Linux VM](https://docs.microsoft.com/en-us/azure/developer/jenkins/configure-on-linux-vm), and then continue with [Step 4](#step4) below to resume PythonSelenium setup after you've created your Jenkins instance.)

----------

### Step 0. Clone the [PythonSelenium](/) repo from GitHub to get started quickly.

### Step 1. Find Jenkins in the Azure Marketplace

#### Search for ["Jenkins" in the Azure Marketplace](https://portal.azure.com/#blade/Microsoft_Azure_Marketplace/GalleryFeaturedMenuItemBlade/selectedMenuItemId/home/searchQuery/jenkins/resetMenuId/) and select the ``Jenkins (Publisher: Microsoft)`` result to get to the Jenkins Start page.

----------

### Step 2. Launch a Jenkins instance

#### Click "Create" and follow the steps...

----------

#### Continue to "Additional Settings" when you're done with "Basics".

----------

#### On the "Additional Settings" section, set the Size to "B2s":

----------

#### Once you've reached Step 5, click "Create" to complete the setup.

----------

### Step 3. Inspect your new Jenkins instance to SSH into the new machine

#### Once your new Jenkins instance has finished launching, you should be able to see the main page:

----------

#### On the main page, you should be able to find the Public IP Address.
* **Use that IP Address to SSH into the machine:**

```bash
ssh USERNAME@IP_ADDRESS
```

----------

<a id="step4"></a>

### Step 4. Clone the PythonSelenium repository from the root ("/") directory.

```bash
cd /
sudo git clone <repo>
```

### Step 5. Enter the "linux" folder

```bash
cd PythonSelenium/integrations/linux/
```

### Step 6. Give the "jenkins" user sudo access (See [jenkins_permissions.sh](/integrations/linux/jenkins_permissions.sh) for details)

```bash
./jenkins_permissions.sh
```

### Step 7. Become the "jenkins" user and enter a "bash" shell

```bash
sudo su jenkins
bash
```

### Step 8. Install dependencies (See [Linuxfile.sh](/integrations/linux/Linuxfile.sh) for details)

```bash
./Linuxfile.sh
```

### Step 9. Start up the headless browser display mechanism: Xvfb (See [Xvfb_launcher.sh](/integrations/linux/Xvfb_launcher.sh) for details)

```bash
./Xvfb_launcher.sh
```

### Step 10. Go to the PythonSelenium directory

```bash
cd /PythonSelenium
```

### Step 11. Install the [requirements](/requirements.txt) for PythonSelenium

```bash
sudo pip install -r requirements.txt --upgrade
```

### Step 12. Install PythonSelenium (Make sure you already installed the requirements above)

```bash
sudo pip install -e .
```

### Step 13. Install chromedriver

```bash
sudo pythonselenium install chromedriver
```

### Step 14. Run an [example test](/examples/my_first_test.py) in Chrome to verify installation (May take up to 10 seconds)

----------

```bash
pytest examples/my_first_test.py --headless --browser=chrome
```

### Step 15. Secure your Jenkins machine

#### Navigate to http://JENKINS_IP_ADDRESS/jenkins-on-azure/

----------

#### Initially, Jenkins uses only ``http``, which makes it less secure.

#### You'll need to set up SSH Port Forwarding in order to secure it.

* **To do this, copy/paste the string and run it in a NEW command prompt on your local machine (NOT from an SSH terminal session), swapping out the username and DNS name with the ones you set up when creating the Jenkins instance in Azure.**

``ssh -L 127.0.0.1:8080:localhost:8080 USERNAME@DNS_NAME``

### Step 16. Login to Jenkins

#### If you've correctly set up SSH Port Forwarding, the url will be ``http://127.0.0.1:8080/``

----------

#### You'll need to get the password from the SSH terminal on the Linux machine to log in:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

### Step 17. Customize Jenkins

----------

### Step 18. Create an Admin user

----------

### Step 19. Create a new Jenkins job

* **Click on "New Item"**
* **Give your new Jenkins job a name (ex: "Test1")**
* **Select "Freestyle project"**
* **Click "OK"**

----------

### Step 20. Setup your new Jenkins job

* **Under "Source Code Management", select "Git".**
* **For the "Repository URL", put PythonSelenium repo.**

----------

* **Under "Build", click the "Add build step" dropdown.**
* **Select "Execute shell".**
* **For the "Command", paste:**

```bash
cd examples
pytest my_first_test.py --headless
```

----------

#### Click "Save" when you're done.

* **You'll see the following page after that:**

----------

### Step 21. Run your new Jenkins job

* **Click on "Build Now"**
* **(If everything was done correctly, you'll see a blue dot appear after a few seconds, indicating that the test job passed.)**

----------

### Step 22. See the top Jenkins page for an overview of all jobs

----------

### Step 23. Future Work

If you have a web application that you want to test, you'll be able to create PythonSelenium tests and add them to Jenkins as you saw here. You may want to create a Deploy job, which downloads the latest version of your repository, and then kicks off all tests to run after that. You could then tell that Deploy job to auto-run whenever a change is pushed to your repository by using: "Poll SCM". All your tests would then be able to run by using: "Build after other projects are built". 

#### Congratulations! You're now well on your way to becoming a build & release / automation engineer!
