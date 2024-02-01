function ajax(src, callback){
    fetch(src)
    .then(function(response){
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    }).then(function (data) {
        callback(data);
    }).catch(function (error) {
        console.error('Fetch error:', error);
    });
}


function render(data){
    let products = document.createElement('div')
    for (let item in data) {
        console.log(data[item])
        let each_product = document.createElement('div')
        
        let nameContent = document.createElement('p')
        let priceContent = document.createElement('p')
        let descriptionContent = document.createElement('p')

        nameContent.textContent = data[item]['name'];
        priceContent.textContent = data[item]['price'];
        descriptionContent.textContent = data[item]['description'];

        each_product.appendChild(nameContent);
        each_product.appendChild(priceContent);
        each_product.appendChild(descriptionContent);

        products.appendChild(each_product);
    }
    
    
    document.body.appendChild(products);
}


ajax("https://remote-assignment.s3.ap-northeast-1.amazonaws.com/products",
    function(response){ 
        render(response);
    }); 