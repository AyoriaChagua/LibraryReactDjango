from rest_framework.views import APIView
from rest_framework.decorators import api_view
from core.serilizers import *
from core.models import *
from rest_framework.response import Response

@api_view(['GET'])
def user_api_view(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serilizer = UserSerializer(user, many = True)
        return Response(user_serilizer.data)

@api_view(['GET'])
def autor_api_view(request, pk):
    if request.method == 'GET':
        if pk is not None:
            autor = Autor.objects.filter(id = pk).first()
            autor_serilizer = AutorSerializer(autor)
            return Response(autor_serilizer.data)

@api_view(['GET'])
def book_api_view(request, pk):
    if request.method == 'GET':
        if pk is not None:
            book = Book.objects.filter(id = pk).first()
            book_serilizer = BookSerializer(book)
            return Response(book_serilizer.data)

@api_view(['GET'])
def books_api_view(request):
    if request.method == 'GET':
        books = Book.objects.all()
        book_serilizer = BookSerializer(books, many = True)
        return Response(book_serilizer.data)



@api_view(['GET', 'POST'])
def loan_api_view(request):
    if request.method == 'GET':
        loans = Loan.objects.all()
        loan_serilizers = LoanSerializer(loans, many = True)
        return Response(loan_serilizers.data)

    elif request.method == 'POST':
        loan_serilizer = LoanSerializer(data = request.data)
        
        if loan_serilizer.is_valid():
            loan_serilizer.save()
            return Response(loan_serilizer.data)
        return Response(loan_serilizer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def loan_detail_api_view(request, pk):
    if request.method == 'GET':
        if pk is not None:
            loan = Loan.objects.filter(id = pk).first()
            loan_serilizer = LoanSerializer(loan)
            return Response(loan_serilizer.data)

    elif request.method == 'PUT':
        loan = Loan.objects.filter(id = pk).first()
        loan_serilizer = LoanSerializer(loan, data = request.data)

        if loan_serilizer.is_valid():
            loan_serilizer.save()
            return Response(loan_serilizer.data)

        return Response(loan_serilizer.errors)

    elif request.method == 'DELETE':
        loan = Loan.objects.filter(id = pk).first()
        loan.delete()
        return Response('Deleted')
