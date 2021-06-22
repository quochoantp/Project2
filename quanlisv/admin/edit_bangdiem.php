<?php include('../includes/header.php'); ?>
<?php include('../includes/mysqli_connect.php'); ?>
<?php include('../includes/functions.php'); ?>
<?php include('../includes/sidebar-admin.php'); ?>

<?php
// Xac nhan bien GET ton tai va thuoc loai du lieu cho phep
if (isset($_GET['cid'])) //&& filter_var($_GET['cid'], FILTER_VALIDATE_INT, array('min_range' =>1))) 
{
    $cid = $_GET['cid'];
} else {
    redirect_to();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Gia tri ton tai, xu ly form
    $errors =  array();
    if (empty($_POST['ma1'])) {
        $errors[] = "ma1";
        echo "<p class='warning'>Không lấy được dữ liệu tên học sinh </p>";
    } else {
        $htSV = $_POST['ma1'];
    }
    if (empty($_POST['mh1'])) {
        $errors[] = "mh1";
        echo "<p class='warning'>Không lấy được dữ liệu mã môn học </p>";
    } else {
        $maMH = $_POST['mh1'];
    }

    // Kiem tra diemlan1
    if (empty($_POST['diemquatrinh'])) {
        $errors[] = "diem_lan1";
        echo "<p class='warning'>Không lấy được dữ liệu message diem qua trinh </p>";
    } else {
        $diemlan1 = $_POST['diemquatrinh'];
    }

    //Kiem tra diem lan 2
    if (empty($_POST['diemcuoiki'])) {
        $errors[] = "diem_lan2";
        echo "<p class='warning'>Không lấy được dữ liệu message diem cuối kì </p>";
    } else {
        $diemlan2 = $_POST['diemcuoiki'];
    }

    if (empty($errors)) {
        // Nếu không có lỗi xả ra thì chèn vào csdl.
        $q = "UPDATE diemmonhoc SET diemquatrinh = {$diemlan1}, diemcuoiki = {$diemlan2} where diemmonhoc.MaMH= '{$maMH}' and diemmonhoc.MaSV=(select MaSV from thongtinsinhvien where Hoten='{$htSV}')";
        $r = mysqli_query($dbc, $q) or die("Query {$q} \n<br/> MySQL Error: " . mysqli_error($dbc));

        if (mysqli_affected_rows($dbc) == 1) {
            $messages = "<p class='success'>Sửa điểm thành công.</p>";
        } else {
            $messages = "<p class='warning'>Kết nối đến Database bị lỗi.</p>";
        }
    } else {
        $messages = "<p class='warning'>Vui lòng điền đầy đủ thông tin các trường</p>";
    }
} // Ket thuc main IF submit
?>
<div id="content">
    <?php
    $q = "SELECT diemquatrinh, diemcuoiki, tt.MaSV, Hoten, mh.MaMH FROM monhoc as mh, thongtinsinhvien as tt, diemmonhoc as d WHERE (mh.MaMH= d.MaMH and tt.MaSV=d.MaSV and Hoten = '{$cid}') ";
    $r = mysqli_query($dbc, $q) or die("Query{$q} \n <br/> MySQL Error: " . mysqli_error($dbc));
    if (mysqli_num_rows($r) == 1) {
        // Neu cac truong ton tai trong bang diem,, dua vao CID, xuat du lieu
        list($Hoten, $MaSV, $diemlan1, $diemlan2) =  mysqli_fetch_array($r, MYSQLI_NUM);
    } else {
        // Neu CID khong hop le se khong the hien thi ra bang diem
        $message = "<p class= 'warning'> Trường này không có.<p>";
    }
    ?>

    <h2>SỬA ĐIỂM CHO SINH VIÊN</h2>
    <?php
    if (!empty($messages)) echo $messages;
    ?>
    <form id="edit_diem" action="" method="post">
        <fieldset>
            <legend>SỬA ĐIỂM</legend>

            <div>
                <label> Ma SV: </label>
                <select name="ma1" tabindex='1'>
                    <?php
                    $q = "SELECT  Hoten FROM thongtinsinhvien";
                    $r = mysqli_query($dbc, $q) or die("Query {$q} \n<br/> MySQL Error: " . mysqli_error($dbc));
                    while ($hien_thi = mysqli_fetch_array($r, MYSQLI_ASSOC)) {
                        echo "<option value='{$hien_thi['Hoten']}'";

                        echo ">{$hien_thi['Hoten']}</option>";
                    }
                    ?>
                </select>
            </div>

            <div>
                <label> Mã môn học: </label>
                <select name="mh1" tabindex='2'>
                    <?php
                    $q = "SELECT MaMH FROM monhoc";
                    $r = mysqli_query($dbc, $q) or die("Query {$q} \n<br/> MySQL Error: " . mysqli_error($dbc));
                    while ($hien_thi = mysqli_fetch_array($r, MYSQLI_ASSOC)) {
                        echo "<option value='{$hien_thi['MaMH']} '";

                        echo ">{$hien_thi['MaMH']}</option>";
                    }
                    ?>
                </select>
            </div>

            <div>
                <label for="diemquatrinh"> Điểm quá trình: <span class="required">*</span>
                    <?php
                    if (isset($errors) && in_array('diem_lan1', $errors)) {
                        echo "<p class='warning'>Vui lòng nhập điểm quá trình cho SV</p>";
                    }
                    ?>
                </label>
                <input type="text" name="diemquatrinh" id="diemquatrinh" value="<?php if (isset($diemlan1)) echo $diemlan1 ?>" size="20" maxlength="150" tabindex="3" />

                </select>
            </div>

            <div>
                <label for="diemcuoiki"> Điểm cuối kì: <span class="required">*</span>
                    <?php
                    if (isset($errors) && in_array('diem_lan2', $errors)) {
                        echo "<p class='warning'>Vui lòng nhập điểm cuối kì cho SV</p>";
                    }
                    ?>
                </label>
                <input type="text" name="diemcuoiki" id="diemcuoiki" value="<?php if (isset($diemlan2)) echo $diemlan2 ?>" size="20" maxlength="150" tabindex="4" />

                </select>
            </div>



        </fieldset>
        <p><input type="submit" name="submit" value="ADD ĐIỂM" /></p>
    </form>

</div>
<!--end content-->
<?php include('../includes/footer.php'); ?>