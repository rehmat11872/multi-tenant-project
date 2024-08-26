from django.shortcuts import render, get_object_or_404
from .models import Product
from tenants.models import Domain

def tenant_product_list(request):
    print('Debug: Accessing tenant_product_list view')
    domain = request.get_host()  # Get the current domain from the request
    print(f'Debug: Current domain - {domain}')
    tenant = get_object_or_404(Domain, domain=domain).tenant  # Fetch tenant using domain
    print(f'Debug: Found tenant - {tenant}')
    products = Product.objects.filter(tenant=tenant)  # Filter products by tenant
    print(f'Debug: Number of products - {products.count()}')
    return render(request, 'shop/product_list.html', {'products': products, 'tenant': tenant})