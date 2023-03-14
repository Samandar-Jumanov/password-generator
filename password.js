
let symbols =['@', '$', '!', '*',')', '(', '+']
 let numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
let letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'X', 'W', 'Z']

 const getPassword =(length , hasLetters , hasNumbers , hasSymbols)=>{
    const available = [
        ...(hasLetters? letters: []),
        ...(hasNumbers? numbers: []),
        ...(hasSymbols? symbols: []),
    ]
    
    let password =''
    if(available.length === 0) return ''

    for (let i = 0; i <length; i ++){
        const random = Math.floor(Math.random() * available.length)
        password+=available[random]
    }
  console.log(password )
 }

 getPassword(12,  true , true , true)

//Works only in Terminal !!!!!!!





  
