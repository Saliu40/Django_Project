from django.db import models

# we Created the file models.py here.
class NewsModel(models.Model):
    description = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=1000, null=True)
    url = models.CharField(max_length=1000, null=True)
    content = models.CharField(max_length=1000, null=True)
    #add more fields as needed
    #we created &added the above Class
    
    class Meta:
        db_table = 'blog'
        #specifiying our custom table name to be blog

        #note, anytime we made adjustment here, we need to perform a makemigrations and migrate for our database to recorgnize the adjustment