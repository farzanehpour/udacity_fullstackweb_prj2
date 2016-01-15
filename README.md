<h1>Tournament project Version 1.0.0</h1>

<p>This is the second assignment for Udacity full stack web developers nanodegree 
program. For more information about the course, please visit:
<a href="https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004">Udacity  nanodegree program</a></p>

<h2>How to run:</h2>

<h3>Create database tables and views via schema (tournament.sql)</h3>

<ol>
<li><p>If you are using vagrant that has been provided by udacity course:</p>

<p>1.1.  Connect to your virtual environment by running following commands:</p>

<pre><code>vagrant up
vagran ssh
cd /vagrant/tournament
vagrant@vagrant-ubuntu-trusty-32:$/vagrant$psql
vagrant=&gt; \i tournament.sql
tournament=&gt; \q
</code></pre></li>
<li><p>If you have postgre installed on your server or your local machine:</p>

<p>2.1.  As database priviledged user, create database tournament in sql bash or by pgAdmin III tool.</p>

<p>2.2.  Connect to tournament database.</p>

<p>2.3.  Open tournament.sql in sql editor, comment out three first lines (drop, create and \c tournament) and run the rest of script.</p></li>
</ol>

<h3>Run tournament-test.py via python:</h3>

<p>In the virtual environment, run the following command line in your tournament folder: </p>

<pre><code>vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py
</code></pre>

<hr />

<h2>deliverable</h2>

<ol>
<li><p>tournament.py -> the main script file that contains required the methods for creating, deleting or defining Swiss tournament tournaments, players and matches. For more information, see <a href="https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true">Project Instruction</a>.</p></li>
<li><p>tournament_test.py-> unit test for tournament methods.</p></li>
<li><p>tournament.sql --> Database schema. </p></li>
<li><p>Readme.md --> this file.</p></li>
</ol>

<hr />

<h2>What can be done more</h2>

<p>This is my first delivery for review. There are more cool stuffs are needed to be done :</p>

<ol>
<li><p>Modify the code so same player can not be choses as his own opponent.</p></li>
<li><p>Implementing odd number of players and bye count.</p></li>
<li><p>Supporting games where a draw is possible.</p></li>
<li><p>Implementing OMW.</p></li>
</ol>

<h2>Student's name:</h2>

<hr />

<p>Shiva Farzanehpour (farzanehpour@gmail.com)</p>
