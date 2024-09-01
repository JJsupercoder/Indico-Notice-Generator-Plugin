
1. Check for a Virtual Environment:

Navigate to your Indico project directory and look for a directory with a name similar to your virtual environment. Common virtual environment names are typically "venv," "env," or "virtualenv." The structure might look like this:
/path/to/your/indico-project/
├── venv/  # or 'env' or 'virtualenv' or a custom name
├── other_project_files

If virtual Environment found then skip this step and go to next.
Otherwise do 


python3 -m venv venv


This command creates a virtual environment named "venv" in your plugin directory.

2. Activate the Virtual Environment:

Depending on your operating system, use one of the activation commands to activate the virtual environment. Replace /path/to/your/plugin with the actual path to your plugin directory:


source /path/to/your/plugin/venv/bin/activate


3. Install Dependencies:

While the virtual environment is activated, you can use pip to install the necessary dependencies for your plugin. 


pip install indico
pip install xhtml2pdf


4. Install the Plugin:

Install your plugin in your Indico virtual environment using pip. Make sure you provide the correct path to your plugin directory:


pip install -e /path/to/your/plugin/directory


5. Update Indico Configuration:

Update the Indico configuration to include your plugin. Edit the indico.conf file (often located at /etc/indico/indico.conf) and add your plugin to the list of plugins to load:


[global]
...
plugins = indico-plugin1, indico-plugin2, indico-pdf-generator 
...


6. Restart Your Indico Instance:

After updating the configuration, restart your Indico instance to apply the changes. You can do this using the systemctl command:


sudo systemctl restart indico


7. Access Your Plugin:

Your plugin should now be available within your Indico instance. Access it through the URL or route you defined in your blueprint


https://your-indico-instance.com/generate_pdf


8. Test the Plugin:

Click on the 4 buttons and see if they all work as intended.


9. Deactivate the Virtual Environment only after testing all things and closing the system:

To deactivate the virtual environment when you're done working on your plugin, simply run


deactivate
