/* eslint-disable @typescript-eslint/no-explicit-any */
import { createClient } from "@/lib/server";

export async function getData(tableName: string) {
  const supabase = await createClient(); // إزالة await إذا كانت createClient ليست async

  try {
    const { data, error } = await supabase
      .from(tableName)
      .select(
        `
        *,
        likes_count(id, likes_count)
      `
      )
      .limit(100);

    if (error) {
      console.error(`Error fetching data from table '${tableName}':`, error);
      return null; // العودة بقيمة null عند وجود خطأ
    }

    return data; // إرجاع البيانات عند نجاح الطلب
  } catch (unexpectedError) {
    console.error("Unexpected error occurred:", unexpectedError);
    return null; // العودة بقيمة null عند حدوث خطأ غير متوقع
  }
}
export async function getDataOnePalette(tableName: string) {
  const supabase = await createClient(); // إزالة await إذا كانت createClient ليست async

  try {
    const { data, error } = await supabase
      .from(`colors`)
      .select(
        `
          *,
          likes_count(id, likes_count)
        `
      )
      .eq(`id`, tableName)
      .single();

    if (error) {
      console.error(`Error fetching data from table '${tableName}':`, error);
      return null; // العودة بقيمة null عند وجود خطأ
    }

    return data; // إرجاع البيانات عند نجاح الطلب
  } catch (unexpectedError) {
    console.error("Unexpected error occurred:", unexpectedError);
    return null; // العودة بقيمة null عند حدوث خطأ غير متوقع
  }
}

export async function getDataSingleTag(tags: string) {
  const supabase = await createClient();

  try {
    console.log("Searching with tags:", [`${tags}`]);

    const { data, error } = await supabase
      .from("colors")
      .select(`*, likes_count(id, likes_count)`)
      .contains("tags", [`${tags}`])
      .limit(80);

    if (error) {
      console.error("Error fetching data with tag:", error);
      return null;
    }

    return data;
  } catch (unexpectedError) {
    console.error("Unexpected error occurred:", unexpectedError);
    return null;
  }
}
