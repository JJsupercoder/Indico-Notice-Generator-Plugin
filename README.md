
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


4. Install the Plugin:

Install your plugin in your Indico virtual environment using pip. Make sure you provide the correct path to your plugin directory:


pip install -e .


5. Update Indico Configuration:

Update the Indico configuration to include your plugin. Edit the indico.conf file (often located at /etc/indico/indico.conf) and add your plugin to the list of plugins to load:


[global]
...
plugins = indico-plugin1, indico-plugin2, indico-pdf-generator 
...


6. Restart Your Indico Instance:

Start the postgresql and redis-server

sudo service postgresql start
sudo service redis-server start


After updating the configuration, restart your Indico instance to apply the changes. 
Run the commands in the terminal in the dev/indico/src or similar directory

indico run -h localhost -q --enable-evalex

in other terminal parallely-
./bin/maintenance/build-assets.py indico --dev --watch



7. Access Your Plugin:

Your plugin should now be available within your Indico instance. Access it through the URL or route you defined in your blueprint


https://localhost/pdf-generator-plugin/event/<event_id>

8. Test the Plugin

9. Deactivate the Virtual Environment only after testing all things and closing the system:

To deactivate the virtual environment when you're done working on your plugin, simply run


deactivate
