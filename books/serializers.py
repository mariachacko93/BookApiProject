from rest_framework import serializers
from books.models import Book,Author
from books import models

class Authorserializer(serializers.ModelSerializer):
   
    class Meta:
            model=Author
            fields=["author"]
                                                
    
class BookSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField( 
                    view_name='details', 
                    lookup_field='pk'
                ) 

    author=Authorserializer(many=True)

    class Meta:
        model=Book
        fields=["id","url","bookname","author","pages","pubyear","abstract"]
        # fields="__all__"

 
    def create(self, validated_data):
        # first we pop or get the the type of the data we want
        author = validated_data.pop('author')
        # then we create an object  of book to put created data into it
        book = models.Book.objects.create(**validated_data)
        for author in author:
            author, created = models.Author.objects.get_or_create(author=author['author'])
            book.author.add(author)
        book.save()
        return book

    
#    using try block
#     def update(self, instance, validated_data):
#         authors_list = []
#         try:
#             author = validated_data.pop('author')
#             for author in author:
#                 print(author)
#                 author, created = Author.objects.get_or_create(author=author['author'])
#                 authors_list.append(author)
#         except:
#             for i in instance.author.all():
#                 authors_list.append(i)
#         instance.author.set(authors_list)
#         instance.bookname = validated_data.get('bookname', instance.bookname)
#         instance.pubyear=validated_data.get('pubyear', instance.pubyear)
#         instance.pages = validated_data.get('pages', instance.pages) 
#         instance.abstract = validated_data.get('abstract', instance.abstract)
#         instance.save()
#         return instance
   
   
   
# with if condition
    def update(self, instance, validated_data):
        author_data = validated_data.get('author')
        # author = instance.author.all()
        # author = list(author)
        instance.bookname = validated_data.get('bookname', instance.bookname)
        instance.pubyear=validated_data.get('pubyear', instance.pubyear)
        instance.pages = validated_data.get('pages', instance.pages) 
        instance.abstract = validated_data.get('abstract', instance.abstract)
        instance.save()

        if author_data:
            author_list=[]
            for auth in author_data:
                author,create = Author.objects.get_or_create(author=auth['author'])
                author_list.append(author)

            instance.author.set(author_list)
        instance.save()
        return instance

    ###################################

