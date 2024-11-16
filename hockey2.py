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
            margin: 20px;
        }
        header, footer {
            padding: 20px;
            background-color: #f8f8f8;
        }
        .product-container {
            max-width: 800px;
            margin: 0 auto;
        }
        .breadcrumb {
            font-size: 14px;
            margin-bottom: 20px;
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
    <!-- Шапка -->
    <header>
        <div class="breadcrumb">Home / Apparel / BAUER TEXTURED FULLZIP SENIOR</div>
    </header>
    <!-- Основной блок продукта -->
    <main>
        <div class="product-container">
            <!-- Название продукта -->
            <h1 class="product-header">Bauer Textured Fullzip Senior</h1>

            <!-- Изображение продукта -->
            <div class="product-images">
                <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhITExMWFhUXGBgXFxcWFxgeGhgaGhcXFhgXHRgaHCggGholHRgVITEhJSkrLi4wFyAzODMsNygtLisBCgoKDg0OGxAQGC0mIB4tLS0vMC0tLS8tLTAuLTAuLS0tLSstKy0tMisrLS0rLS0tLS0tLS0tKy0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAAAwIEBQYHCAH/xABFEAABAwIDBAcFBQYDCAMAAAABAAIRAyEEEjEFQVFhBgcTInGBkTKhscHwI0JSgtEUYnKSouEINbMVM1NzdJOy8TTD0v/EABkBAQEBAQEBAAAAAAAAAAAAAAABBAIDBf/EACERAQEAAgMAAwEAAwAAAAAAAAABAhEDEiExQVFxBBMy/9oADAMBAAIRAxEAPwDuKIiAiIgIiICIiAiIgIiICIiAittpY1tGlUrP9mm1z3eDRPquQ9LutR5I/ZnOp03QMxa0nQzFrXi5JnhxlykWY2uzouE9F+tmvRBbWaa9Mk5HufDhe4LoJ3OsfKwXXei3SOjjqIq0jB0ewkZmHgQNx1B3hSZSrcbGZREXTkREQEREBERAREQEREBERAREQEREBEWodPOsDD7NAa4GrXcJZRYQDG5z3fcaTaYJMGAYMBt6Lgm0eu/GObFLD0aRP3nF748B3RPMyqdmddeNDvtaVCo07mtcwiwFjmOsHUHXyXPaOutd9Ra/0M6WUtoUe0pjI9sCpTJksJ0vvaYMGBodFsC6ciIiDm/XB0l7NlPZ9K9bEQXAAHLSkg673uaWjwcbQFpNfq5xYoNe5zA4CBTF4sREmxmfctl2rhhW6QPc6IotpmTua2mKkcAMz5nmtxr7ewxIYal3WbZ0E8jEe9ZeXL3xq4sfPh55GxK4DqRYQQTAIsNZM8DmOiyGwtt4jZlenWaLgZXMPs1G72ki4nUHcWg8QerdI6+HogCo6HHQAOLjM7gCVoXS+i2rSLqY7zIc5rmkHLcTlImOa5w5Lv2PTPixmPld62VtGniKNOvSOanUaHtOljxG47iFdrRupnEB2zKbAZ7J9Sn/AFdoB6PC3la4xUREVQREQEREBERAREQEREBERAREQfHGASuEbL6LnaeJxGJrm1R75IO4HK0DiIAA5ALuWMpF1N7QYLmuAPAkEStE6EvpUMFhhUqMY51Nrjmc0SXXm55rw58rNae/BjLvbWNqdWTSA2m6ABckcFofSToucIRqR+LiV3/H4ym1pc57Q38RIiOMrTdsV6VVrolwcIEsdB8CRCzzkylaf9eNjTeqHaRo4+lJhtQmk7cO8Dl8e+G+q9ErzFgZw2La0gnLUa8GNMpDptuhenGukAjQrXx3bHyTT6iIvR5tK/2a47SxNZzMofSZTGknK90u829n9BfavR1vbNeXv7t4LyQfIQtk2lSiHjUW9foLXczy9xfTqEPEB7XNaGAE2kvaQTEzvWLOayu2/iss8a9t/CZ9oS57g00w0ZTFzoQYsVa7R2Dka+kHulzHAFxzRIO/eE6U4V1N/antXG0AvY6TMiGtfePkr2pnrPp05Ae8AX0BcLTHKSY4Ln16ZakXPUtnbQq05BptyOBjSo41BVbO+A2l6ro6xXRrYjMJQFJl7lz3RGZx1MbtAPLfqsqtuMsnr5+dly8ERF04EREBERAREQEREBERAREQEREHwhaLW6NF9JlFtepTFNvZEMIbmyw1r3HKSYDbDS5sbRva1HpkKrbUp+0LZixiQHQTv09V4c/xL+NH+N/1Z+sV0gwAZh6DMxytqDM628ROkC5HorPaHR6lRJrh9QkiMudxaRGsEx5xK+bcL6tJhYKrGiO4TRbEd2DL5ER+ixGExFR9KoILWUyGMkzmOkj934x5nJdxu1PtgOkWHipSqNGpueAA18iR9Bd32DiRUw9F43sbPiBB94K8/wDSjG/aUKYdqHTG8Zm29y671ZYwuwwaToAR6Q4eoHqtPDdX+sfPqzz6bkiItLKjxFEPaWnQj04Fa3Q2gxvcqkNcOOh5jksH157drYbZ+Wg4tfWeKZe0kFrA1znwRoTDW+DiqaGNw1XAYariajKYdRpuzPe1urATcm91n5p7GjhvlUdJK9Bt8wJ3X+rLC7I2yyjWbiaxPZ08znECSBBDnRqYB3XgWXzb2wKVKHNfM3HMLWullbs8M9gsXtLfUX90ryxns098rbLt6IY4EAgyDcEaEcV9XGOqTp+yjTODxtVrGUwBRqvcABYTRJPC5aeRFoaF2HCYplVgfTe17HXa5jg5pHEOFitrAmREQEREBERAREQEREBERAREQEREBYfpRXayjmMTmblnxlx8Mocte6UdZNPAYo0K+Fr5YBZVZkIeCASQHOFgSRqTLTbSdK6U9PG1R2s5gWzSpiYa073HnYHfYtGpjy5b5qT5enFPd/jacftDDPpOc6o5k6tmBOpkb/JaNj9sZszKLSGC5c6wAEy4k+JV51b0qtehiK1US2pWzMJ3w0Nc7wkAflK1rpptbtCaVAxRaYc+32jtIHFvx10hZccLc+v43ZcusO1YDH7Sa+u17v8AdsGVsi5GrnRrefQBdd6mtqNqVHta4OGQkcjLDEbjquJNaCbd/dMGByB+pV/0a27WwOIFSk7K8HhLSDq1w+8w+trQRK2dJ5r6Ye9939vW6wPSjpdhMA2a9TvES2kzvVH+DOHMwOa5l0t64q2RlPC0uxc9gc6q+HQTqKQ0MH7zv5dCuY18Q973VKhL3vMue4y4niSbk/ou3m2Pp303q7RqNDmNp0mZuzYLk5soLnuNi6wgAACTrqtZqMBpBpLiREEncPu8mju2HBV5Z104AKsYcAOMO01Jj3Sitz6K7cpvw/Y1XtYaMAOe4Adl7TdbmBLfILn239smviKtSSGkwxp3NHs24wJPMlTVMPmeGj7wjyD9PRR4zZrGRqSSFxjhJbXeXJbjIsWy65+ufisrsfaGIwr+0w2IdRd+46zuTm+y/wAHAr52LI/UL5iMO0CwPou3m6t0Z66yIZtCjy7ajfzdTPvLT4NXVtibcw2Lp9phqzKrLTlN2k3hzT3mO5OAK8nljMom0gK/6ObRqYOu2vRqFrmwNTB712uH3m8vmJQeskWM6ObZZi8PTrs+8O8PwuFnN8j8lk0BERAREQEREBERAREQERfHFB5/6381TEGo5xJa6A06NaDGWPEFadsLYoq1KdOfs6r2iQYzNnM8yYIyta46btVd9KNrOr1K7iQ67rtPdu97gQYuId6FYMmo+mxrCQAwA3jXceUbl5YzLrr9euVnZuvTfrHADsHgWs7ADs3VAD3wNWU4IApx3ZvmkxbXW8NmqNBqgDg1o91zr8Fa4XZzWwQMz+e7iQr+zYkiRe3P4rvDCYzUc5ZXK7qVhEGW28oAWEqtzPtutfgZ+QPor3G1XE5QYzOAHo0k+gJ8laVIaTHGPygZQPQn3LpyqxmJJpNYROW7TvaZgj+E8Nxy8SocLUJVeEE5mzBgwee7ymPVWmFcM1piURlWs4hS1GRECx1PAKPJER81KwHe4+Ab+qChrHAtdBvOUkGHRq4cQC46bxClNNxsXOP5QBPiriliXO7BpADGNq5DvINQOcDfcTbTXmqcU0l7SCCL2mLkQioq7DADR9b7qGpUc3VhI8ldPltyAPF5VrjsUHAgEDwRFGJe0hojdvVi4yTyn3Zj8wo3gg2d6mV8omT4iSeViT6AeqDrvUZ0hLar8K82qy5vJ4Gb3jP/ACtXbl5H2FtN1Coyuz2mvFQflNh4d33r1lgsS2rTp1WGWva17TxDgHD3FBMiIgIiICIiAiIgIiICwXTrGGls/G1GmHCjUDTwc5pa0+pCzq5t16bVNPB0qAP+/qd7mymM5H8/Z+h4oOE4gzTLRIBgc4EK6wrO7Atx5ngrZrsxBvAvHPX9PRXWHqXuLeCKqp1ADANzvU1TCtcPfMkL7iC2O9HmrHHYruOynTTy0VDDXqkzOWWt9wPmIP8AMoMY2PUqfZdKGn08T9R6JtJlp4fP6CCywru8rdhIe7KPvED1KkoG4UL8wquyxqojOUKbyJLo5AH4khSYlpcIDo5Df5wom5nNu6PDf5nQKZmCaLm/Mud8BCKipsc6owWyNa9oFxq8F0nfJ+rKYsYxzQ5rBvm9o5+Uea+UKoa4E6DOf6oCgqYpj3tvy46oPuPxFOoQJ3+Sx78O0G/uEK8ruDNRIsdANCsVWxDXExYHdKqIcU7ny8lMH5WuPl+g+f8AKrbE04g6q7wYkAndeOeo9/wQV6Q3hDf/ANe+V6X6pNpdts2iJl1KaLvywWj+RzF5noCSTw+J+iu0dQ20+/icOTq1lVo/hOR5/qp+ig7EiIgIiICIiAiIgIiIC4R197RzY3DURpRpFxPOq648hSafzLu68xdY21XVNrYmoBmayqGAH2fsoZB5EtJ80GtZ3NqOaRcEtOliCQR7lePxIasW+o6Iub3PE/MrJYKoHC40jdBlBNTe18kgRun61VhtWi1rbHU5YvdXGJxLGkgETvWKxlXNUYJsD5Kqy1EgNDS6OTfaPIcBzUW0nCA1rYGp8dwn3+YVxgaA9o3+f9uSttpaygsqZuFAQ7tHxc5ncLXKmCtXUwaj5Md4/EqIzGGwpIlz7cA6PeP7K5a4OGQSd2/XfPz9NytMHlMNnuzcnf8AX6LJvbTa2zGnyCohs58br+gd+ikxGIayJvrrHh8Vj6NQ5p0jNPrMKp9djiJ/soqCvimu1/FPko6pETCuqxa0Tl38+AIN/JWNWpm+6VUWuIIIMCIHBTbNfbQk30VFVt4jdKlpUn0+xduqsLxB3CpUpG269N30UF12cNO4DdzOg5nefIDetw6pMaKW1MNc9/PTP5mmB4Zgz0Wn1K8wLAC+71JV90bxbmYqg5jHOLa1JwgakVGkX33Cg9bIiICIiAiIgIiICIiDHdI9o/s2ExOI/wCFSqVBzLWEgeZAXkqiHgnOZJuTMyeM716P65Noilsuu0kA1iykJ3y7M8f9ttRebKZddx0j0QSYGo4WItz3+SqbjQHXEA24KKo5+YE2iPH6usg2uzKXEbpKotalKnMCLcuXqsXWA7QZTpF/7KWtihcgRJNhwnT4qPD0p8zc+8+6fUIL2lTrtMCT4ZiD6CFPWe4jvNII1Oo9RopMNimNaB978QMDlorLaFdzj3i4DdOnog+NCtg4Zjm0n5qfDvv4X9LqLBgEwfqUGTw+HouE+e5VAUib+yNGzA8XO+ACgZUpNdEd3fGpPArK4evSiWtj4hBbU2tLtO6SYA4RbRSVsQymbNv52O7wUYq3JIOpNtdLKB2I4s8BBhFW9XFFziS0lVPqQJLY4SFLiKgaLNAVm6u5xki/NEU1QYJ0+o+a2DH4LtdlYLFU4Bw9Spg6okycz34mk4DePtKgPOPLC4lndv8Ah09D8lkNi1i7Z20aOcDK/C4jKY7wbUdQdHAzWpGf3Y3qC0wWFBEkSeLtI5DRZHo+xgxmHLwcgrUsxzAENFRuY3sBE8FbYKj3BJPkY+Bv5q1rPLZIJtJ+t6D2MihwYcKbA4y7K3MeJgSbc1MgIiICIiAiIgIiIOIf4h9oZ6uDwgdENfWcObiKdMn0q+q5E2kcpaLu0tfQyFsnWftUYnaWLqA+zU7FlwRlpAU5BG4ua9w/jWtMa5tgbk2MoLluKcG3bJG6FC0h4LSIMSJ9N6+YSq9joImdZ+YKvnvaLCzjoB8uBsqMLUAEjfxWWwTXAGGzeQYPy5z6rGuoyXH7rT6xrHK59Fn8M6KYcCNJ5Ef+kFljMSN9Ak8g4e+Fi6peSTlIHA/3WQxG0CeXgbK2pOzOBJnf/ZBA1+UGRqCB52PuX2jVykWXzGm7Rwn3wrzZ9QEZS2Y+rIL2jXpOnu3F/K3vlUtrtNg0BusHT9PWyiGIbMey3kP1V9TxoNmskIqLV+m/QXHsiAJ3aL7isUKZaAy9ptEX3DXdE/Qp7QTPM6R+HnY+KtH1O9ME+PNEW9bEuc6T6K4qVSORiVRXxDpsI4QFauDiZg+iCV1WQ6RHdt6QvuxXnJjI30WA+H7Vhj8QFb1idDwhbX0W2Pm2XtnE5SS0Yakw+OJpVKnmAyn6qCyw5hix5GYxIGYxJ0E2nwGq+is4NAIJ/hJjzi6odmuY05fAb0Hshoiy+q12XSLKNFriSW02NJOshoBnmrpAREQEREBERAREQeQelGHaMdjmezlxNcDgA2q8R8FjshhpB0vr4LZetSk1u18a3Qdq1xj96mxx+JWsdiSIaZjhvvqgucRiHwLa71cUHscxxIuAZnwj4KDC1nN7rxbdIt4L6HNccrRAJi3CdFRGyGtixJmRumII8LKJ+JdGQQG8ApdpVLgfebY84NvdCtS3Qzru3oPm9VCpGn0f0UVR+4a7+SlwtP0CCnFN+0E8BHx+Mq6pVHNM5SB5e9ZTCbKa/A4/EuINSk7DU2j8IqOc5zuU5Q0fm88bhcW4QCP7hQX9PHtIOZlxxn4qF+MncAOAi++5OqhNV5M5T/L9cl9fiyRBAtxaPmqpUrS4RGvLgvlTEvG6PBWueXSpixw0B+SIja6oTYH0P6KSq2oNdfK36KmvXeTGYzwCpdhX74HiUET6Z/EPqxXYeglGnW6N7Tp0we0HbVH7w57WMewt3wRTaP4gVyZwpinp3515em+f6fXoXVpVrUtj7bqgEMcxjGOH4yHsqZTxDX0/coNEGcMkk39lonfvPMq96O0c2LwjTecRQDr8arAQFQ9oyEg94i3LwG5R7OrOw9WlXa6H0ntqjM2fYcHRE20/9Kj18ipY6QCNCJVSgIiICIiAiIgIiIPOPXvsg0dpGuQcmJptc0/vU2tpPb5AUz+dc8pD2SDyjevR/XR0Sq47CU3UG5qtBxeGb3tLYe1v71mkDfBGpC82uYZNiCDodQd4g/BBfVqVThMcxI8NLaKKpVyw7LDheePiFXRxTsse6P1UTaL6kwBa5EgGN5jh+o4qiGticxzEX+KhJnQQpTTPD1PxVMeHxQUNYrjDC4HEhReUK5wTe8PEIOrdTGApHDbafi6TXYU9mXB8EEUhWqutqIDmEHjpcW5KGH2gAAbht7chJmBzW24LFPZQxYpOjtaL6TxeHN1FvxA6Hm4bytYw75aPBTG7dZY6Qiq4X+a+OrkzZTVFEWwunL7SpzJ5W8Z38olVVakbroKsR9fW9VF0x6lBQMU4aT6CfXVQuc43Ku4C+ZVBaFp4r0l1f1adfYGHZXbna5j6DmSROWo9gEi4OVoMi41XnOoF17qqxHZ4Kk0ucRVrVS0HQEDKY8ck+Mrjky6zb04sO+Wk+O6AYNjDka9vM1Hyf6lP1ddXGEOJfXqB7zRLcjHEFmYl3eIiXQWiATC2Ha1bu+YA+vf5K96u3d/E31yH3vv71m4ssu3taebDGYeRuyIi1sQiIgIiICIiAiIgLg3X90bpUqtDFUmBnbl4qkSA6oMrmuI0Bc3tJMXLZPFd5Wndbew/2vZmIa0S+kBXZaTNOS4AcSwvaP4kHl6mY5/XJXjMQyN/hfw58eKsSwQPVfMnM+qolr1sx0EDQblbkoWqkhBVKz7dkVMP2RqtLTWpNq053seO64eiu+rLoodo41lJwPYs+0rn9wGzJ4uMN8Mx3L0H1g9Fm4zDtyNHbUO9SgC4gZqfg4AWtdrVzfh1j8uWbH6NUmYClinFxfWfWa9pIgBrixuVvCGEk8XRwXMX0uzqVKe5riBPDcum43oriBWpYhtCvSeO6IpE5tbEBpN5i6550lpPZjK4qgh+YSHNym7WkS2LWIsuMLez25ZJjP6x7zKozkKpyicV7MwXqphUJOq3PrF2B+x4igySc+EwziSN7afYu8L0pjmoNZbWO8KTMo2k+I96SqKapXaeg2HJw+EOUBtKgKlvxP7g83Z6h/K5cVeF1nqm2PiKmCqdg0fa1ofUcYDQxgyNO8j7R7rA/wC8HBeXLjuPfgy61fY7aji+sRcNho/iM28YLb/vLduq3Cn9nfXdc1XQ08WMsCPFxd7lHsDq9bTObE1BV72fI0FrcwywSZlwAaBEDmt5XHHx6u675uaZTUERF7MwiIgIiICIiAiIgL4QvqIPJfT7ZDcHj8Vhmewx8s5NqNbVa38oeG/lWvyts62ak7Xxx/fYPSlTb8lqBKoEqhfVt/VX0a/btoUWOE0qR7atwysILWH+J2URwzcEHdOqPot+w4BmZsV68VavESO5T/K0xHEu4rdkRQF566/9hto42liWn/5TTmbwfRFNhPgWup24tPFehVx7/EdhZoYGr+Gq9n87A7/6vcg4Y9RPUtVQuXSPuGw7qj2U2CXPcGNHEuIaB6ldt/xCbNhuz63AVKLjxMMez/xqLk3Q2kXY/AtaJJxNCP8AutM+knyXobrw2b22y6jwJNCpTrDwk03HwDajj5KK83L5K+lUKo+kr0r1H042RRMzmfWPhFVzAPRo8oXmhekOoYn/AGSyf+LWjwzfrKlV0RERQEREBERAREQEREBERAREQeUOs/8AzXH/APNP/i1aqV9RUUrtf+Gz2to+GH+NdESjt6IigLlv+Ij/AC7D/wDVs/0cQiIPP1bVQFEXSNk6tP8ANcB/z2/NelusL/K9of8ATVv9NyIuVeT3KhEXSKWr0z1I/wCUYf8Ajr/61REUqt8REUBERAREQEREH//Z" alt="Main Product">
                <img src="data:image/jpeg;base64,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" alt="Thumbnail 1">
                <img src="data:image/jpeg;base64,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" alt="Thumbnail 2">
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
                    <img src="data:image/jpeg;base64,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" alt="Recommendation 1">
                    <p>Bauer Waffle Toque Senior - $29.99</p>
                    <button onclick="addToCart()">Add to Cart</button>
                </div>
                <div class="recommendations-item">
                    <img src="data:image/jpeg;base64,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" alt="Recommendation 2">
                    <p>Bauer Colorblock Toque Senior - $29.99</p>
                    <button onclick="addToCart()">Add to Cart</button>
                </div>
            </div>
        </div>
    </main>
    <!-- Подвал -->
    <footer style="text-align: center; margin-top: 40px;">
        &copy; 2024 Bauer. All Rights Reserved.
    </footer>
</body>
</html>
