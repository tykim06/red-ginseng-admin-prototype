from import_export import resources
from .models import Customer
from import_export.fields import Field

class CustomerResource(resources.ModelResource):
    name = Field(attribute='name', column_name='이름')
    phone_number = Field(attribute='phone_number', column_name='전화번호')

    class Meta:
        model = Customer

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dataset.insert_col(0, col=["",]*dataset.height, header="id")
