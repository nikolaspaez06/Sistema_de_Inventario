from models.supplier import Supplier as SupplierModel
from schemas.supplier import Supplier 


class SupplierService():
    def __init__(self,db):
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result 


    def create_supplier(self,supplier:SupplierModel):
        new_suppler = SupplierModel(
            sub_name = supplier.sub_name,
            address = supplier.address,
            phone = supplier.phone,
            email =  supplier.email

        )
        self.db.add(new_suppler)
        self.db.commit()
        return
    
    
    def get_for_id(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id). first()
        return result

    def update_supplier(self, id: int, data: Supplier):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id == id).first() 
        supplier.sub_name = data.sub_name
        supplier.address = data.address
        supplier.phone = data.phone
        supplier.email = data.email
        self.db.commit()
        return

    def delete_supplier(self,id:int):
        self.db.query(SupplierModel).filter(SupplierModel.id == id).delete()
        self.db.commit()
        return