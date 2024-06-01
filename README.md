The API allows for managing orders, products, and order items.

List Products: GET /api/products/

Create Product: POST /api/products/

Retrieve Product: GET /api/products/{id}/

Update Product: PUT /api/products/{id}/

Partial Update Product: PATCH /api/products/{id}/

Delete Product: DELETE /api/products/{id}/

List Orders: GET /api/orders/

Create Order: POST /api/orders/

Retrieve Order: GET /api/orders/{id}/

Update Order: PUT /api/orders/{id}/

Partial Update Order: PATCH /api/orders/{id}/

Delete Order: DELETE /api/orders/{id}/

perl
Copy code

### Step 3: Create API Documentation

You can use tools like Swagger or Postman to check the API. For Django, To do that you can use the `drf-yasg` package to generate Swagger documentation.

#### Using `drf-yasg` for API Documentation

1. **Install `drf-yasg`**:
   ```sh pip install drf-yasg

Configure drf-yasg in urls.py:

# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Orders API",
        default_version='v1',
        description="API documentation for Orders application",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@orders.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]