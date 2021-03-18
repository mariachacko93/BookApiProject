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

    author=Authorserializer(many=True,read_only=True)

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

    def partial_update(self, instance, validated_data,partial=True):
        author = validated_data.pop('author')
        instance.abstract = validated_data['abstract']
        instance.bookname=validated_data['bookname']
        instance.pubyear=validated_data['pubyear']

        instance.pages=validated_data['pages']

        # instance.author = validated_data['author']
        # instance.publication_date = validated_data['publication_date']
        authors_list = []
        for author in author:
            author, created = models.Author.objects.get_or_create(author=author['author'])
            authors_list.append(author)
        instance.author.set(authors_list)
        instance.save()
        return instance 