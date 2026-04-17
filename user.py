import hashlib

class User:
  def __init__(self, id, name, password, role):
    self.id = id
    self.name = name
    self.role = role

    # hashing the password before storing it
    hash_obj = hashlib.sha256(password.encode())    # encode string to bytes
    hex_dig = hash_obj.hexdigest()      # get hexadecimal digest
    self.password = hex_dig
    # You can't "unhash" it — hashing is one-way.


  # this is 2nd construtor which accepts the already hashed password
  @classmethod
  def from_db(cls, id, name, password, role):
    user = cls.__new__(cls)  # creates empty User object without calling __init__
    user.id = id
    user.name = name
    user.password = password  # already hashed, assign directly!
    user.role = role
    return user

  # checking a password
  def check_password(self, password):

    # hash the received password
    input_password = hashlib.sha256(password.encode()).hexdigest()
    
    # checking if the passwords match
    return input_password == self.password
  
    # if input_password == self.password:
    #   return True
    # else:
    #   return False

  # allow user to change password
  def change_password(self, old_password):

    if old_password.strip() == "":
      raise ValueError("Password cannot be empty. ")
    
    else:
      if self.check_password(old_password):
        new_password = input("Enter your new password: ")

        if new_password.strip() == "":
          raise ValueError("Password cannot be empty.")
        
        else:
          self.password = hashlib.sha256(new_password.encode()).hexdigest()

      else:
        raise ValueError("Incorrect password!")

      
  # to check if the user is amin or not  
  def is_admin(self):
    return self.role.lower() == "admin" 


# user = User("asdf", "bishal", "baniya", "admin")
# print(user.change_password("baniya"))