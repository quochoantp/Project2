<?php include('../includes/header.php'); ?>
<?php include('../includes/mysqli_connect.php'); ?>
<?php
if (isset($_SESSION['userid']) == null) {
	include('../includes/sidebar-a.php');
} else {
	include('../includes/sidebar-admin.php');
}
?>
<div id="content">
	<h2 style="text-align:left;">Kế hoạch</h2>
	<a href="https://ctt.hust.edu.vn/DisplayWeb/DisplayKeHoach?kehoach=25101">
		<p><strong> Kế hoạch thu học phí K65 học kì 1 năm học 2020-2021(20201-Đợt 1)</strong></p>

		<div>
			Phòng Đào tạo thực hiện việc tính toán học phí cho mỗi học kỳ theo 02 đợt:
			Đợt 1: tính toán sơ bộ học phí cần đóng;
			Đợt 2: tính toán chính xác học phí của mỗi sinh viên trong học kỳ đang học.
			<p>
				Thời gian đóng học phí:
				Từ 8h00 ngày 02/11/2020 đến 16h00 ngày 15/11/2020
			</p>

			<p> ________________________________________________________________________

			</p>
		</div>
	</a>
	<a href="https://ctt.hust.edu.vn/DisplayWeb/DisplayKeHoach?kehoach=25107">
		<p><strong> Kế hoạch thu học phí kì 20201-Đợt 2</strong></p>

		<div>
			Sinh viên có thể tra cứu học phí học kỳ 20201 (đợt 2) từ ngày 14/12/2020 bằng cách:<br>

			Đăng nhập tài khoản Cổng thông tin đào tạo vào mục Thông tin công nợ học phí
			<p>
				Thời gian đóng học phí:<br>

				Bắt đầu đóng học phí đợt 2 từ ngày 14/12/2020 đến 16h00 ngày 29/01/2021
			</p>

			<p> ________________________________________________________________________

			</p>
		</div>
	</a>
	<a href="https://ctt.hust.edu.vn/DisplayWeb/DisplayKeHoach?kehoach=25119">
		<p><strong> Kế hoạch học tập và công tác đào tạo trong tình hình mới(cập nhật 7/6/2021)</strong></p>

		<div>
			Kính gửi các em sinh viên, học viên cao học và nghiên cứu sinh,<br>
			Nhà trường trân trọng gửi đến các em những thông tin quan trọng nhất về công tác đào tạo và kế hoạch học tập trong điều kiện dịch Covid-19 diễn biến hết sức phức tạp và nguy cơ lây nhiễm cao như sau:
			<p>
				Tiếp tục triển khai hình thức dạy-học trực tuyến (online) đối với toàn bộ các lớp học phần lý thuyết/bài tập của các khóa từ K64 về trước đến hết ngày 19/6/2021 và đến hết ngày 03/7/2021 đối với K65 (chi tiết xin xem tại mục 5).
			</p>
			<p> ________________________________________________________________________

			</p>
		</div>
	</a>
</div>
<!--end content-->

<?php include('../includes/footer.php'); ?>