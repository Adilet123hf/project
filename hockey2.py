<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bauer Textured Fullzip Senior</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .product-container {
            max-width: 800px;
            margin: 0 auto;
        }
        .product-header {
            text-align: center;
        }
        .product-images {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }
        .product-images .main-img {
            width: 60%;
            max-width: 500px;
            margin-bottom: 10px;
        }
        .product-images .thumbnail {
            width: 5%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .product-images img {
            width: 120px;
            height: auto;
        }
        .product-info {
            margin: 20px 0;
        }
        .add-to-bag {
            background-color: #000;
            color: #fff;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            display: block;
            margin: 10px 0;
        }
        .add-to-bag:hover {
            background-color: #444;
        }
        .product-overview {
            border-top: 1px solid #ddd;
            padding-top: 20px;
        }
        .product-overview h2 {
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 0;
        }
        .product-overview .features {
            display: none;
            margin-top: 10px;
        }
        .product-overview .features ul {
            list-style: none;
            padding: 0;
        }
        .product-overview .features li {
            margin-bottom: 5px;
        }
        .toggle-icon {
            font-size: 20px;
            margin-left: 10px;
        }
        .sizes,
        .quantity {
            margin: 20px 0;
        }
        .sizes select,
        .quantity input {
            padding: 5px;
            font-size: 14px;
        }
        .recommendations {
            margin-top: 30px;
        }
        .recommendations img {
            max-width: 100px;
            display: block;
        }
        .recommendations-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 10px 0;
        }
        .recommendations-item p {
            margin: 0 10px;
            flex-grow: 1;
        }
        .recommendations button {
            background-color: #000;
            color: #fff;
            padding: 5px 15px;
            border: none;
            cursor: pointer;
        }
    </style>
    <script>
        function addToCart() {
            alert("Товар добавлен в корзину!");
        }

        function toggleOverview() {
            const features = document.querySelector('.features');
            const icon = document.querySelector('.toggle-icon');
            if (features.style.display === 'none' || features.style.display === '') {
                features.style.display = 'block';
                icon.textContent = '−';
            } else {
                features.style.display = 'none';
                icon.textContent = '+';
            }
        }
    </script>
</head>
<body>
    <div class="product-container">
        <!-- Название продукта -->
        <h1 class="product-header">Bauer Textured Fullzip Senior</h1>

        <!-- Изображение продукта -->
        <div class="product-images">
            <img src="https://www.bauer.com/products/bauer-textured-fullzip-senior" alt="Main Product">
            <img src="https://www.bauer.com/cdn/shop/files/1064087_HOL24_APPAREL_TEXTURED-FULLZIP_SR_WHT_0539_600x.png?v=1727122264" alt="Thumbnail 1">
            <img src="https://www.bauer.com/cdn/shop/files/1064087_HOL24_APPAREL_TEXTURED-FULLZIP_SR_WHT_0590.png?v=1727205924" alt="Thumbnail 2">
        </div>

        <!-- Информация о продукте -->
        <div class="product-info">
            <p><strong>$99.99</strong></p>
            <p>Earn 99 Loyalty Points for this product. Log in or Sign Up. Terms Apply.</p>
            <p>Pay in 4 interest-free installments of $24.99 with ShopPay. Learn more.</p>
        </div>

        <!-- Размер и количество -->
        <div class="sizes">
            <label for="size">Size:</label>
            <select id="size">
                <option>S</option>
                <option>M</option>
                <option>L</option>
                <option>XL</option>
                <option>XXL</option>
            </select>
        </div>
        <div class="quantity">
            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" value="1" min="1">
        </div>

        <!-- Кнопка Add to Bag -->
        <button class="add-to-bag" onclick="addToCart()">Add to Bag - $99.99</button>

        <!-- Product Overview -->
        <div class="product-overview">
            <h2 onclick="toggleOverview()">
                Product Overview
                <span class="toggle-icon">+</span>
            </h2>
            <div class="features">
                <p>Take this puffer jacket anywhere – literally. The Bauer Hockey FLC Packable Puffer is right at the sweet spot of light enough for everyday wear, yet warm enough for cold nights on the pond.</p>
                <h3>Key Features:</h3>
                <ul>
                    <li>• 100% recycled nylon</li>
                    <li>• Tapered hockey fit</li>
                    <li>• Lightweight PrimaLoft® Black Insulation ThermoPlume®</li>
                    <li>• Bonded quilted panels</li>
                    <li>• YKK® zippers</li>
                    <li>• Encased elastic on hem and sleeves</li>
                </ul>
            </div>
        </div>

        <!-- Рекомендации -->
        <div class="recommendations">
            <h2>You'll Also Love</h2>
            <div class="recommendations-item">
                <img src="https://example.com/recommend1.jpg" alt="Recommend 1">
                <p>Bauer Waffle Toque Senior - $29.99</p>
                <button onclick="addToCart()">Add to Cart</button>
            </div>
            <div class="recommendations-item">
                <img src="https://example.com/recommend2.jpg" alt="Recommend 2">
                <p>Bauer Colorblock Toque Senior - $29.99</p>
                <button onclick="addToCart()">Add to Cart</button>
            </div>
        </div>
    </div>
    <footer style="text-align: center; margin-top: 40px;">
        © 2024 Bauer. All Rights Reserved.
    </footer>
</body>
</html>
