## Streamlit App to Display NER output of Flask API

> It's a Streamlit App which uses Flask API created by me which in return give JSON file with Named Entity Recognition on scrapped data of Wikipedia and extracted entities like city, person, organisation, Date, Geographical Entity, Product etc.


### Feature
- It displays annotated text in Streamlit App for each Named Entity.
- User can give their input in Text Field provided.
- It's a simple but easy to understand Streamlit app.

![alt text](https://cdn.pixabay.com/photo/2021/04/12/21/08/21-08-33-456_1280.jpg)


### How to RUN

**This procedure is useful for MAC/LINUX. I'm not sure about Windows.**

**Step 1:**
Frst Install python and pip in Your system. You can find many tutorials and blog online. (Ignore if already installed)

**Step 2:**
Install Virtial Environment "virtualenv" so that your local Python Dependencies are untouched when installing this Project's dependencies.

```bash
$ pip install virtualenv
```

**Step 4:**

Clone this GITHUB REPO using this Link : https://github.com/Swapnil4Github/Display_NER_Streamlit.git in your desired Directory.

```bash
$ git clone https://github.com/Swapnil4Github/Display_NER_Streamlit.git
```

**Step 5:**
Now you'll be having Project Folder "Display_NER_Streamlit". Navigate to that folder.

```bash
$ cd Display_NER_Streamlit
```

**Step 6:**
Create a Virtual Environment here. You can name anything, but in my case I'm using '_venv_'

```bash
$ virtualenv venv
```

**Step 7:**
Activate the Virtual Environment

```bash
$ source venv/bin/activate
```

Replace the name 'venv' with the name of your virtual environment name, if it's different.

**Step 8:**
Install Dependencies

```bash
$ pip install -r requirements.txt
```

**Step 9:**
Everything's Done!
Now just run the server

```bash
$ streamlit run app.py
```
**Step 7:**
Give Input through text field to perform NER on it with help of Flask API

Now go to you browser's search box and paste the server IP **127.0.0.1:8000/



&copy; Swapnil Srivastava 2021
