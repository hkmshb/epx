{% extends 'base.tpl' %}
{% block content %}
    <div class="row">
        <div class="toc columns three">
            <br/>
            <ul>
                <li><a href="#about">About {{ app.name }}</a></li>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#starting-app">Starting Application</a></li>
                <li><a href="#app-ui">Application GUI</a></li>
                <li><a href="#modus">Modus Operandi</a></li>
            </ul>
        </div>
        <div class="content columns nine">
            <section><a name="about"></a>
                <h2>About {{ app.name }}</h2>
                <p>
                    It is a utility program for extracting ePin (electronic-pin)
                    numbers (for mobile airtime) embedded within an xml file
                    created using the Android Backup & Restore app.
                </p>
            </section>
            
            <section><a name="installation"></a>
                <h2>Installation</h2>
                <p>
                    NO INSTALLATION WHAT-SO-EVER REQUIRED. The application is bundled 
                    and distributed as a compressed file (.7z, .tar.gz, or .zip), which 
                    extracts to a single directory name <em>{{ app.name }}</em>. The 
                    top-level contents of this directory are two subdirectories
                    <em>assets</em> and <em>bin</em> (which contains the actual application 
                    binaries) and two files, <em>{{ app.name }}.bat</em> and <em>help.html</em>.
                </p>
                <p style="margin-left:80px;">
                    {{ app.name }}/ <br/>
                        &nbsp;&nbsp; +-- assets/  <br/>
                        &nbsp;&nbsp; +-- bin/  <br/>
                        &nbsp;&nbsp; +-- {{ app.name }}.bat  <br/>
                        &nbsp;&nbsp; +-- help.html
                </p>
            </section>

            <section><a name="starting-app"></a>
                <h2>Starting Application</h2>
                <p>
                    Launch the application by double-clicking the <em>{{ app.name }}.bat</em>
                    file mentioned above. Note that the application CANNOT BE LAUNCHED using
                    the <em>{{ app.name }}.exe</em> binary within the <em>bin</em> directory.
                </p>
                <p>
                    To ease launching of the application, a shortcut to the '.bat' file
                    can be placed on the desktop.
                </p>
            </section>

            <section><a name="app-ui"></a>
                <h2>Application GUI</h2>
                <p>
                    The application's graphical user interface (GUI) is as depicted in the
                    picture below.
                </p>
                <img alt="{{ app.name }} ui" src="./assets/imgs/app-ui.png" />
                <p>
                    <table>
                        <caption>GUI Buttons</caption>
                        <tr><td>Browse</td>
                            <td>Use to select directory containing backed up epin sms files
                                to be processed
                            </td>
                        </tr>
                        <tr><td>Process</td>
                            <td>Initiates the processing of files in the selected directory.<br/><br/>
                                This button is shown after browsing and selecting a directory
                                which has files that can be processed. It also doubles as a Cancel
                                button at some point, which is used to abort and on going processing
                                task.
                            </td>
                        </tr>
                        <tr><td> &nbsp;&nbsp; i </td>
                            <td>The info button; displays an About dialog for the application.</td>
                        </tr>
                        <tr><td> &nbsp;&nbsp; ? </td>
                            <td>The help button; displays this help document.</td>
                        </tr>
                    </table>
                </p>
            </section>

            <section><a name="modus"></a>
                <h2>Modus Operandi</h2>
                <p>
                    <ol>
                        <li>Launch the {{ app.name }} application if it isn't already running.</li>
                        <li>Collect all sms epins backup files to be processed together in 
                            a single directory in any location of your choice; preferably on 
                            the desktop or within a folder on the desktop.</li>
                        <li>Point application to 'Directory to Process', which is the directory 
                            mentioned above, using the 'Browse' button.
                            <ul>
                                <li>The full path of the selected directory is shown in the 
                                    textbox besides the 'Browse' button.</li>
                                <li>The 'Process' button is displayed.
                                <li>The Info line at the button displays a summary of the 
                                    top-level contents of the selected directory in the format: <br/>
                                    <em> sub-directory count</em> / <em>total file count</em> / 
                                    <em>processable file count</em>
                                </li>
                                <li>If processable file count is zero, the 'Process' button 
                                    is disabled otherwise it is enabled.</li>
                            </ul>
                        </li>
                        <li>Click the 'Process' button for the epins extraction and collation
                            operation to begin.
                            <ul>
                                <li>The 'Browse' button is disabled.
                                <li>The 'Process' button text changes to 'Cancel'.
                                <li>If the 'Process' button is not enabled, this indicates that 
                                    though there might be files in the target directory, NO 
                                    PROCESSABLE files were found. Return to (2).
                                </li>
                            </ul>
                        </li>
                        <li>Click the 'Cancel' button anytime before the extraction operation 
                            completes to abort the operation.</li>
                        <li>On extraction completion:</li>
                            <ul>
                                <li>The 'Browse' button is re-enabled.</li>
                                <li>The 'Cancel' button text is changed back to 'Process'.</li>
                                <li>A summary of the operation result is displayed on the Info
                                    line, formatted as thus:<br/>
                                    <em>successfully processed file count</em> /
                                    <em>unsuccessfully processed file count</em></li>
                                <li>A directory name '_passed' is created in the processed directory
                                    and all successfully processed files are copied there in. The
                                    unsuccessfully processed files are left in place.</li>
                                <li>An 'epins.txt' file containing successfully processed epins in 
                                    desired format is created in the processed directory.</li>
                                <li>A 'report.html' file providing extra details on the operation is 
                                    also created in the processed directory. </li>
                            </ul>
                        </li>
                        <li>Return to (1) to begin processing another batch of sms backup files.</li>
                    </ol>
                </p>
            </section>
        </div>
    </div>
{% endblock %}
