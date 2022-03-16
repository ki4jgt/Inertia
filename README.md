# Inertia
Inertia allows users to securely use weak passwords, by hashing them through Argon2, making it safe for them to login using passwords like: God, dog, their name, etc.

# How do we do this?

The most secure passwords are randomly generated. Modern password requirments (1 lowercase letter, 1 number, 1 punctionation mark, etc) actually weaken the security of your data, by making your passwords less random. The brain however, cannot keep up with random strings. And password managers put all your eggs in a single basket. 1 vulnerability, and all your online accounts are being traded on the darkweb.

# Inertia offers a compromise.

Inertia solves all of this, by hashing weak passwords through Argon2, along with a personal salt string generated for you on first run. This is achieved by listening for an activation keyboard sequence, capturing the inputted password, and replacing it with an Argon2 hash containing both your given password, and your personal salt string.

# Why?

Unlike a password manager, which is compromised by a master password, Inertia uses 3 key authentication to slow down hackers:

- Your master password: entered when you start the program
- Your salt string: Encrypted on disk with the master password
- And your site-specific password.

*You only technically have to remember the master password*

Inertia allows you to use any password you want. You can use site-specific data like a company name, domain name, homepage content, or a word that reminds you of the site. You can use DNS records, or your pet's name. Inertia allows you to keep your login information in your head, by using easy-to-remember cryptographically-secured passwords.

# Instructions
**Inertia is in BETA, and is not suited for production use.**

To use Inertia:

- Set the script to run on user login/system startup
- Run it
- Enter your master password
- Find a place where you'd like a cryptographically-secured password
- Enter the activation sequence ```@/```
- Enter your weak password
- Enter the activation sequence again

Your weak password will be replaced with a secure 20 character string.
