import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details, hash, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.product_description = product_description
        self.shipment_details = shipment_details
        self.hash = hash
        self.nonce = nonce

class SupplyChainBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(
            0, "0", int(time.time()),
            "GenesisProduct", "GenesisSupplier",
            "GenesisDescription", "GenesisShipment",
            self.calculate_hash(0, "0", int(time.time()), "GenesisProduct", "GenesisSupplier", "GenesisDescription", "GenesisShipment", 0),
            0
        )
        self.chain.append(genesis_block)

    def add_supply_record(self, product_id, supplier_id, product_description, shipment_details):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        previous_hash = previous_block.hash
        nonce = self.proof_of_work(index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details)
        new_hash = self.calculate_hash(index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details, nonce)
        new_block = Block(index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details, new_hash, nonce)
        self.chain.append(new_block)

    def proof_of_work(self, index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details):
        nonce = 0
        while True:
            new_hash = self.calculate_hash(index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details, nonce)
            if new_hash[:4] == "0000":
                return nonce
            nonce += 1

    def calculate_hash(self, index, previous_hash, timestamp, product_id, supplier_id, product_description, shipment_details, nonce):
        value = str(index) + str(previous_hash) + str(timestamp) + str(product_id) + str(supplier_id) + str(product_description) + str(shipment_details) + str(nonce)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(vars(block))

if __name__ == '__main__':
    supply_chain_blockchain = SupplyChainBlockchain()
    supply_chain_blockchain.add_supply_record("Product_1", "Supplier_A", "Widgets", "Shipped on 2023-07-01")
    supply_chain_blockchain.add_supply_record("Product_2", "Supplier_B", "Gadgets", "Shipped on 2023-07-02")
    supply_chain_blockchain.add_supply_record("Product_3", "Supplier_C", "Thingamajigs", "Shipped on 2023-07-03")
    supply_chain_blockchain.print_chain()
