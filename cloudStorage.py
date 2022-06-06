import dropbox

class TransferData:
    def __init__(self , access_token):
        self.access_token=access_token
        
    def uploadMyFile(self , fileFrom, fileTo):
        #link the our dropbox account to the application
        dbx=dropbox.Dropbox(self.access_token)
        f = open(fileFrom, "rb" )
        #upload these contents to the dropbox using the files_upload() method
        dbx.files_upload(f.read(), fileTo)
def main():
    access_token="sl.BJAGMc_D6mQyuteeGjaa1pQGFzAxIAKli4KRO1cpRYSoLZ7aTitKJMxcEee-USwVuerJjtaUcNKZXRnB1-5DW8JZatH_cqSGhgwvza28GfdZ7mki5j9k1ywDdgFj2bAGi_hEEZNinBc"
    #creating object for class
    td=TransferData(access_token)
    
    fileFrom=input("Enter the File Path to Transfer : ")
    fileTo=input("Enter the File Path to Upload to Dropbox : ")
    
    td.uploadMyFile(fileFrom , fileTo)
    print("Files Have Been Sucsessfully Moved")
main()