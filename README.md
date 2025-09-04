
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soundix Checkout</title>
  <style>
    body {
      margin: 0;
      font-family: "Poppins", sans-serif;
      background: #2b2222;
      color: white;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      overflow-x: hidden;
    }

    .container {
      display: flex;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(12px);
      border-radius: 20px;
      padding: 20px;
      width: 90%;
      max-width: 1100px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }

    /* Left Panel */
    .left {
      flex: 1;
      padding: 20px;
    }
    .brand {
      font-size: 24px;
      font-weight: 600;
      margin-bottom: 20px;
    }
    .product-options {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 20px;
    }
    .option {
      width: 50px;
      height: 50px;
      border-radius: 10px;
      border: 2px solid transparent;
      cursor: pointer;
      overflow: hidden;
    }
    .option.active {
      border: 2px solid orange;
    }
    .option img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .main-product {
      width: 280px;
      margin: 20px auto;
    }
    .main-product img {
      width: 100%;
      margin-top: auto;
    }
    .tagline {
      text-align: center;
      margin-top: 15px;
      font-size: 14px;
      color: #ddd;
    }

    /* Right Panel */
    .right {
      flex: 1;
      padding: 20px;
      border-left: 1px solid rgba(255, 255, 255, 0.2);
    }
    .checkout-header {
      display: flex;
      justify-content: space-between;
      font-size: 18px;
      font-weight: 600;
      margin-bottom: 20px;
    }
    .input-group {
      margin-bottom: 15px;
    }
    .input-group input {
      width: 100%;
      padding: 12px;
      border-radius: 10px;
      border: none;
      outline: none;
      font-size: 14px;
    }
    .flex-input {
      display: flex;
      gap: 10px;
    }
    .flex-input input {
      flex: 1;
    }
    .summary {
      margin-top: 20px;
      font-size: 14px;
    }
    .summary p {
      display: flex;
      justify-content: space-between;
      margin: 6px 0;
    }
    .buy-btn {
      width: 100%;
      padding: 14px;
      background: orange;
      border: none;
      border-radius: 12px;
      color: white;
      font-size: 16px;
      font-weight: bold;
      margin-top: 20px;
      cursor: pointer;
      transition: 0.3s;
    }
    .buy-btn:hover {
      background: darkorange;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Left Section -->
    <div class="left">
      <div class="brand">Soundix</div>
      <div class="product-options">
        <div class="option active"><img src="pic_1-removebg-preview (1).png" alt="black headphones"></div>
        <div class="option"><img src="pic_2-removebg-preview.png" alt="white headphones"></div>
        <div class="option"><img src="pic_3-removebg-preview.png" alt="blue headphones"></div>
        <div class="option"><img src="pic_4-removebg-preview.png" alt="gold headphones"></div>
      </div>
      <div class="main-product">
        <img src="pic_1-removebg-preview (1).png" alt="main headphone">
      </div>
      <p class="tagline">Play and go your own world</p>
    </div>

    <!-- Right Section -->
    <div class="right">
      <div class="checkout-header">
        <span>Checkout</span>
        <span>20,000 /-</span>
      </div>

      <div class="input-group">
        <input type="text" placeholder="Cardholder name">
      </div>
      <div class="input-group">
        <input type="text" placeholder="Card Number">
      </div>
      <div class="flex-input">
        <input type="text" placeholder="MM">
        <input type="text" placeholder="YY">
        <input type="text" placeholder="CVV">
      </div>

      <div class="summary">
        <p><span>Balance amount :</span><span>15,000 /-</span></p>
        <p><span>Vat (21%) :</span><span>500 /-</span></p>
        <hr>
        <p><strong>Total :</strong><strong>20,000 /-</strong></p>
      </div>

      <button class="buy-btn">Buy</button>
    </div>
  </div>
</body>
</html>
