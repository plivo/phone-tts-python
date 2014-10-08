# Text to Speech Application

Text to Speech is an easy method to add voice to your phone capabilities.
This function can be used to deliver spoken versions of text such as live
information (e.g., sports scores) and important messages (e.g., emergency updates).
Examples of simple changes in the code can allow you to change the message,
the voice (e.g., male or female), who will be receiving your message, and much more.

The instructions below will teach you build your own Text to Speech app that
can make an outbound call to any phone number or have Plivo read out a text-based message

## Prerequisites

1. Sign up for a free developer trial account at [Plivo.com](https://manage.plivo.com/accounts/register/).

2. Head over to the [Heroku documentation](https://devcenter.heroku.com/articles/quickstart),
    setup an account, and install the [Heroku toolbelt](https://toolbelt.heroku.com/).

    <div class="doc-note">Note: You may also use your own servers, but to simplify things, we will use Heroku.</div>


## Get the application source code


1. Clone the source files from github by typing the following command into your console:

        git clone https://github.com/plivo/phone-tts-python.git


    <div class="doc-note">Note: If you don’t already have pip installed, you'll want to follow this <a href="http://www.pip-installer.org/en/latest/installing.html">guide</a>.</div>

2. Run the app locally. In your console, navigate to the folder `phone-tts-python` and run the app,
    by typing the following into your console:

        cd phone-tts-python
        virtualenv --distribute venv
        source venv/bin/activate
        pip install -r requirements.txt
        python app.py


## Understand the XML

When a call comes in, the XML is what controls the call and
tells Plivo what to do with that call. The XML element which will be
used in this call flow is `<Speak>`. The `<Speak>` element reads out the
text that is specified.

Hack Tip: Change the <Speak> XML attributes to see how it affects your call.
For example, change WOMAN to MAN or change en-US to en-GB. Visit the [Speak XML](/docs/xml/speak/) docs
for exact details on the element attributes.

Click [http://localhost:5000/response/ivr/](http://localhost:5000/response/speak/) to access your app XML and verify it the
same XML as shown below.

{% highlight xml %}
<Response>
    <Speak language="en-US" loop="1" voice="WOMAN">
        Congratulations! You just made a text to speech app on Plivo cloud!
    </Speak>
</Response>
{% endhighlight %}


## Deploy your app on Heroku

Create a Heroku app by typing the following commands into your console:

    heroku create
    git push heroku master
    heroku scale web=1


<div class="doc-note">
Your output should look like the following. Make a note of your Heroku app URL. In this case, the Heroku app URL is http://pacific-chamber-7397.herokuapp.com/
</div>


    Creating pacific-chamber-7397... done, stack is cedar
    http://pacific-chamber-7397.herokuapp.com/ | git@heroku.com:pacific-chamber-7397.git
    Git remote heroku added



## Create a new Plivo application

1. Sign into your Plivo account.

2. Create a Plivo application by clicking on the 'New Application' button in the [Applications](https://manage.plivo.com/app/) tab.

3. Give a name to your application (next to Application Name), lets call it 'Phone TTS'.

4. Fill in the Answer URL field with your Heroku app URL appended by **/response/speak/**

    For example, our Answer URL will look like this:

        http://pacific-chamber-7397.herokuapp.com/response/speak/

5. Choose the GET Answer method and leave all other fields as is. Click on 'Create' to save.

![Phone IVR App](https://www.plivo.com/assets/docs/create-application-phone-tts.png)


## Assign a Plivo phone number to your app

1. Go to the [Numbers](https://manage.plivo.com/number) tab and select the phone number you want to use for this app. If you don't have a number, click on the [Buy Number](https://manage.plivo.com/number/search/) button to purchase one.

2. Then select 'Phone IVR' (name of the app) from the Plivo App dropdown list.

3. Click 'Update' to save.


![Edit Number](https://www.plivo.com/assets/docs/edit-number-phone-tts.png)


Call your Plivo phone number to see how the Text to Speech application works.


Is anything on this page unclear? [Suggest edits and help us improve our documentation!](/contact/support/)
