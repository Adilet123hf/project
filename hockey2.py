<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bauer Textured Fullzip Senior</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header, footer {
            padding: 20px;
            background-color: #f8f8f8;
        }
        .breadcrumb {
            font-size: 14px;
            margin: 20px;
        }
        .product-container {
            display: flex;
            gap: 20px;
            margin: 20px;
        }
        .product-images {
            flex: 2;
        }
        .product-images img {
            max-width: 100%;
            margin-bottom: 10px;
        }
        .product-details {
            flex: 3;
        }
        .product-details h1 {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .price {
            font-size: 20px;
            color: #000;
            margin-bottom: 10px;
        }
        .size-chart {
            margin-bottom: 10px;
        }
        .buy-container {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .buy-container button {
            padding: 10px 20px;
            background-color: #000;
            color: #fff;
            border: none;
            cursor: pointer;
        }
        .recommendations {
            margin: 20px;
        }
        .recommendations h2 {
            margin-bottom: 10px;
        }
        .recommendation-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }
        .recommendation-item img {
            max-width: 80px;
        }
        .recommendation-item button {
            padding: 5px 10px;
            background-color: #000;
            color: #fff;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <!-- Шапка -->
    <header>
        <div class="breadcrumb">Home / Apparel / BAUER TEXTURED FULLZIP SENIOR</div>
    </header>

    <!-- Основной блок продукта -->
    <main>
        <div class="product-container">
            <!-- Блок с изображениями -->
            <div class="product-images">
                <img src="main-product.jpg" alt="Main Product">
                <img src="product-thumbnail1.jpg" alt="Thumbnail 1">
                <img src="product-thumbnail2.jpg" alt="Thumbnail 2">
            </div>

            <!-- Детали продукта -->
            <div class="product-details">
                <h1>Bauer Textured Fullzip Senior</h1>
                <p class="price">$99.99</p>
                <p>Earn 99 Loyalty Points for this product. Log in or Sign Up. Terms Apply.</p>
                <p>Pay in 4 interest-free installments of $24.99 with ShopPay. Learn more.</p>

                <div class="size-chart">
                    <label for="size">Size:</label>
                    <select id="size">
                        <option>S</option>
                        <option>M</option>
                        <option>L</option>
                        <option>XL</option>
                        <option>XXL</option>
                    </select>
                </div>

                <div class="buy-container">
                    <label for="quantity">Quantity:</label>
                    <input type="number" id="quantity" value="1" min="1" style="width: 50px;">
                    <button>Add to Bag - $99.99</button>
                </div>
            </div>
        </div>

        <!-- Секция рекомендаций -->
        <div class="recommendations">
            <h2>You’ll Also Love</h2>
            <div class="recommendation-item">
                <img src="recommendation1.jpg" alt="Recommendation 1">
                <div>
                    <p>Bauer Waffle Toque Senior</p>
                    <p>$29.99</p>
                </div>
                <button>Add to Cart</button>
            </div>
            <div class="recommendation-item">
                <img src="recommendation2.jpg" alt="Recommendation 2">
                <div>
                    <p>Bauer Colorblock Toque Senior</p>
                    <p>$29.99</p>
                </div>
                <button>Add to Cart</button>
            </div>
        </div>
    </main>

    <!-- Подвал -->
    <footer>
        <p>&copy; 2024 Bauer. All Rights Reserved.</p>
    </footer>
</body>
</html>
