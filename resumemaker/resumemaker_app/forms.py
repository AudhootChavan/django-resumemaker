from django import forms
from django.core import validators

#Here we will set form fields


class resume_form(forms.Form):

    #Name
    full_name = forms.CharField(widget = forms.TextInput( attrs = { 'class' : 'form-control','placeholder' : 'Eg. John Doe'}) , label = 'Full Name:')

    #Contact Information

    mobile = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control', 'placeholder' : '91 - 9833 - 222222'}),label = 'Mobile: ')

    email = forms.EmailField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'johndoe@gmail.com'}),label = 'Email: ')

    # catch = forms.CharField( widget = forms.HiddenInput , required= False, validators =  [validators.MaxLengthValidator(0)])
    catch = forms.CharField( widget = forms.HiddenInput , required= False)


    #Summary
    summary = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Aspiring Full Stack Developer with experience in ...', 'rows' : '3'}),label = 'Summary:')

    #Education Details
    education_detail_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Manipal Institute of Technology'}),label = 'School: ', required = False)
    education_detail_1_2 = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Masters of Engineering in Computer Science'}),label = 'Degree: ', required = False)
    education_detail_1_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : ' First Class, CGPA ~ 8.0' , 'rows' : '3'}),label = 'Description: ', required = False)

    education_detail_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Pillai College of Engineering'}),label = 'School: ', required = False)
    education_detail_2_2 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Bachelors of Engineering in Computer Science'}), label = 'Degree: ', required = False)
    education_detail_2_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'First Class, Rank 5th, Overall GPA ~ 7.0 ', 'rows' : '3'}),label = 'Description: ', required = False)

    education_detail_3_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Jamnabai Narsee International School'}),label = 'School: ', required = False)
    education_detail_3_2 = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'High School Diploma'}),label = 'Degree: ', required = False)
    education_detail_3_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : ' Grade A', 'rows' : '3'}), label = 'Description: ', required = False)

    education_detail_4_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Jamnabai Narsee International School'}),label = 'School: ', required = False)
    education_detail_4_2 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : '10th Grade IGCSE'}), label = 'Degree: ', required = False)
    education_detail_4_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Grade A', 'rows' : '3'}),label = 'Description: ', required = False)


    #Work Experience

    experience_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Project Manager'}),label = 'Title: ', required = False)
    experience_1_2= forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Apple Inc'}), label = 'Company: ', required = False)
    experience_1_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Managing teams, Reporting to Team lead ..', 'rows' : '3'}),label = 'Description: ', required = False)

    experience_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Project Manager'}),label = 'Title: ', required = False)
    experience_2_2= forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Apple Inc'}),label = 'Company: ', required = False)
    experience_2_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Managing teams, Reporting to Team lead ..', 'rows' : '3'}),label = 'Description: ', required = False)

    experience_3_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Project Manager'}),label = 'Title: ', required = False)
    experience_3_2= forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Apple Inc'}),label = 'Company: ', required = False)
    experience_3_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Managing teams, Reporting to Team lead ..', 'rows' : '3'}), label = 'Description: ', required = False)

    experience_4_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Project Manager'}),label = 'Title: ', required = False)
    experience_4_2= forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Apple Inc'}),label = 'Company: ', required = False)
    experience_4_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Managing teams, Reporting to Team lead ..', 'rows' : '3'}),label = 'Description: ', required = False)

    #Certifications

    certificate_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Introduction to Computer Science and Programming - Online'}),label = 'Certificate Name: ', required = False)
    certificate_1_2  = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Massachusetts Institute of Technology'}),label = 'Certificate Authority: ', required = False)
    certificate_1_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'certificate-link-dot-com OR Description', 'rows' : '3'}), label = 'Description/Link: ', required = False)

    certificate_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Introduction to Computer Science and Programming - Online'}),label = 'Certificate Name: ', required = False)
    certificate_2_2  = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Massachusetts Institute of Technology'}),label = 'Certificate Authority: ', required = False)
    certificate_2_3 = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'certificate-link-dot-com OR Description', 'rows' : '3'}),label = 'Description/Link: ', required = False)

    certificate_3_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Introduction to Computer Science and Programming - Online'}),label = 'Certificate Name: ', required = False)
    certificate_3_2  = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Massachusetts Institute of Technology'}), label = 'Certificate Authority: ', required = False)
    certificate_3_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'certificate-link-dot-com OR Description', 'rows' : '3'}), label = 'Description/Link: ', required = False)

    certificate_4_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Introduction to Computer Science and Programming - Online'}),label = 'Certificate Name: ', required = False)
    certificate_4_2  = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Massachusetts Institute of Technology'}),label = 'Certificate Authority: ', required = False)
    certificate_4_3 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'certificate-link-dot-com OR Description', 'rows' : '3'}), label = 'Description/Link: ', required = False)


    #Honors and Awards
    award_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Best Business Project Award'}),label = 'Title: ', required = False)
    award_1_2  = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Won award in college business project competition..', 'rows' : '3'}),label = 'Description: ', required = False)

    award_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Best Business Project Award'}),label = 'Title: ', required = False)
    award_2_2  = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Won award in college business project competition..', 'rows' : '3'}),label = 'Description: ', required = False)

    award_3_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Best Business Project Award'}),label = 'Title: ', required = False)
    award_3_2  = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Won award in college business project competition..', 'rows' : '3'}),label = 'Description: ', required = False)

    #Projects

    project_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Library Management System'}),label = 'Title ', required = False)
    project_1_2  = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Web Application built with ..', 'rows' : '3'}), label = 'Description: ', required = False)
    project_1_3 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'project-link-dot-com'}), label = 'Link: ', required = False)

    project_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Library Management System'}),label = 'Title ', required = False)
    project_2_2  = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Web Application built with ..', 'rows' : '3'}),label = 'Description: ', required = False)
    project_2_3 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'project-link-dot-com'}), label = 'Link: ', required = False)

    project_3_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Library Management System'}),label = 'Title ', required = False)
    project_3_2  = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Web Application built with ..', 'rows' : '3'}), label = 'Description: ', required = False)
    project_3_3 = forms.CharField( widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'project-link-dot-com'}),label = 'Link: ', required = False)

    project_4_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Library Management System'}),label = 'Title ', required = False)
    project_4_2  = forms.CharField( widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Web Application built with ..', 'rows' : '3'}),label = 'Description: ', required = False)
    project_4_3 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'project-link-dot-com'}), label = 'Link: ', required = False)


    #Skills

    skills_1_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Programming Languages'}),label = 'Title', required = False)
    skills_1_2  = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Python , JavaScript , HTML ..', 'rows' : '3'}), label = 'Description: ', required = False)

    skills_2_1 = forms.CharField(widget = forms.TextInput( attrs = {'class' : 'form-control','placeholder' : 'Frameworks'}),label = 'Title', required = False)
    skills_2_2  = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Django , Bootstrap ...', 'rows' : '3'}), label = 'Description: ', required = False)


    #Hobbies

    hobby_1_1 = forms.CharField(widget = forms.Textarea( attrs = {'class' : 'form-control','placeholder' : 'Playing Chess , Listening to Music .. ', 'rows' : '3'}),label = 'Hobbies', required = False)

    def clean(self):
        all_clean_data = super(resume_form, self).clean()
        catch = all_clean_data['catch']

        if len(catch) > 0:
            raise forms.ValidationError('INVALID FORM INPUT.')

        return
