from app.models.expert_model import experts_collection

def seed_experts():
    experts = [
        {
            "name": "Dr. Sunita Deshmukh",
            "expertise": "Organic Farming & Bio-fertilizers",
            "organization": "KVK Varanasi",
            "city": "Varanasi",
            "state": "Uttar Pradesh",
            "phone": "9415002233",
            "email": "sunita.deshmukh@kvk.res.in",
            "type": "local"
        },
        {
            "name": "Dr. Amit Maheswari",
            "expertise": "Horticulture & Fruit Preservation",
            "organization": "CISH Rehmankhera",
            "city": "Lucknow",
            "state": "Uttar Pradesh",
            "phone": "9839001122",
            "email": "a.maheswari@cish.gov.in",
            "type": "local"
        },
        {
            "name": "Dr. Preeti Jha",
            "expertise": "Seed Technology",
            "organization": "BHU Agriculture Dept",
            "city": "Varanasi",
            "state": "Uttar Pradesh",
            "phone": "9918003344",
            "email": "preeti.jha@bhu.ac.in",
            "type": "local"
        },
        {
            "name": "Dr. Rakesh Yadav",
            "expertise": "Water Management & Irrigation",
            "organization": "KVK Prayagraj",
            "city": "Prayagraj",
            "state": "Uttar Pradesh",
            "phone": "9721004455",
            "email": "r.yadav@kvk.res.in",
            "type": "local"
        },
        {
            "name": "Dr. Rajesh Kumar",
            "expertise": "Plant Disease Specialist",
            "organization": "KVK Lucknow",
            "city": "Lucknow",
            "state": "Uttar Pradesh",
            "phone": "9876543210",
            "email": "rajesh.kumar@kvk.res.in",
            "type": "local"
        },
        {
            "name": "Dr. Anjali Sharma",
            "expertise": "Soil & Fertility",
            "organization": "KVK Kanpur",
            "city": "Kanpur",
            "state": "Uttar Pradesh",
            "phone": "9123456780",
            "email": "anjali.sharma@kvk.res.in",
            "type": "local"
        },
        {
            "name": "Dr. Vivek Singh",
            "expertise": "Crop Protection",
            "organization": "ICAR Delhi",
            "city": "Delhi",
            "state": "Delhi",
            "phone": "9988776655",
            "email": "vivek.singh@icar.gov.in",
            "type": "global"
        },
        {
            "name": "Dr. Meenakshi Swaminathan",
            "expertise": "Climate Resilient Agriculture",
            "organization": "ICAR-CRIDA",
            "city": "Hyderabad",
            "state": "Telangana",
            "phone": "8899112233",
            "email": "m.swaminathan@crida.res.in",
            "type": "global"
        },
        {
            "name": "Dr. Samuel O'Brien",
            "expertise": "Precision Farming & AI",
            "organization": "IARI (Pusa Institute)",
            "city": "Delhi",
            "state": "Delhi",
            "phone": "7766554433",
            "email": "samuel.obrien@iari.res.in",
            "type": "global"
        },
        {
            "name": "Dr. Lakshmi Narayan",
            "expertise": "Genetic Engineering & GMOs",
            "organization": "TNAU",
            "city": "Coimbatore",
            "state": "Tamil Nadu",
            "phone": "9080706050",
            "email": "l.narayan@tnau.ac.in",
            "type": "global"
        },
        {
            "name": "Dr. Robert D'Souza",
            "expertise": "Post-Harvest Technology",
            "organization": "IIHR Bangalore",
            "city": "Bengaluru",
            "state": "Karnataka",
            "phone": "8123456789",
            "email": "robert.dsouza@iihr.res.in",
            "type": "global"
        }
    ]

    # Clean up old records to prevent duplicates
    experts_collection.delete_many({})
    experts_collection.insert_many(experts)

    print(f"Successfully seeded {len(experts)} experts!")


if __name__ == "__main__":
    seed_experts()